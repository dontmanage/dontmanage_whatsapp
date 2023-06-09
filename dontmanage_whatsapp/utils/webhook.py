"""Webhook."""
import dontmanage
import json

from werkzeug.wrappers import Response


@dontmanage.whitelist(allow_guest=True)
def webhook():
    """Meta webhook."""
    if dontmanage.request.method == "GET":
        return get()
    return post()


def get():
    """Get."""
    hub_challenge = dontmanage.form_dict.get("hub.challenge")
    webhook_verify_token = dontmanage.db.get_single_value(
        "Whatsapp Settings", "webhook_verify_token"
    )

    if dontmanage.form_dict.get("hub.verify_token") != webhook_verify_token:
        dontmanage.throw("Verify token does not match")

    return Response(hub_challenge, status=200)


def post():
    """Post."""
    data = dontmanage.local.form_dict
    dontmanage.get_doc({
        "doctype": "WhatsApp Notification Log",
        "template": "Webhook",
        "meta_data": json.dumps(data)
    }).insert(ignore_permissions=True)

    messages = data["entry"][0]["changes"][0]["value"].get("messages", [])
    if messages:
        for message in messages:
            if message['type'] == 'text':
                dontmanage.get_doc({
                    "doctype": "WhatsApp Message",
                    "type": "Incoming",
                    "from": message['from'],
                    "message": message['text']['body']
                }).insert(ignore_permissions=True)
    else:
        update_status(data["entry"][0]["changes"][0])
    return


def update_status(data):
    """Update status hook."""
    if data.get("field") == "message_template_status_update":
        update_template_status(data['value'])

    elif data.get("field") == "messages":
        update_message_status(data['value'])


def update_template_status(data):
    """Update template status."""
    dontmanage.db.sql(
        """UPDATE `tabWhatsApp Templates`
        SET status = %(event)s
        WHERE id = %(message_template_id)s""",
        data
    )


def update_message_status(data):
    """Update message status."""
    id = data['statuses'][0]['id']
    status = data['statuses'][0]['status']
    conversation = data['statuses'][0].get('conversation', {}).get('id')
    name = dontmanage.db.get_value("WhatsApp Message", filters={"message_id": id})

    doc = dontmanage.get_doc("WhatsApp Message", name)
    doc.status = status
    if conversation:
        doc.conversation_id = conversation
    doc.save(ignore_permissions=True)
