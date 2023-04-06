# Copyright (c) 2022, Shridhar Patil and contributors
# For license information, please see license.txt
import json
import dontmanage
from dontmanage.model.document import Document
from dontmanage.integrations.utils import make_post_request


class WhatsAppMessage(Document):
    """Send whats app messages."""

    def before_insert(self):
        """Send message."""
        if self.type == 'Outgoing' and self.message_type != 'Template':
            if self.attach and not self.attach.startswith("http"):
                link = dontmanage.utils.get_url() + '/'+ self.attach
            else:
                link = self.attach

            data = {
                "messaging_product": "whatsapp",
                "to": self.format_number(self.to),
                "type": self.content_type
            }
            if self.content_type in ['document', 'image', 'video']:
                 data[self.content_type.lower()] = {
                    "link": link,
                    "caption": self.message
                }
            elif self.content_type == "text":
                data["text"] = {
                    "preview_url": True,
                    "body": self.message
                }

            elif self.content_type == "audio":
                data["text"] = {
                    "link": link
                }

            try:
                self.notify(data)
                self.status = "Success"
            except Exception as e:
                self.status = "Failed"
                dontmanage.throw(f"Failed to send message {str(e)}")

    def notify(self, data):
        """Notify."""
        settings = dontmanage.get_doc(
            "WhatsApp Settings", "WhatsApp Settings",
        )
        token = settings.get_password("token")

        headers = {
            "authorization": f"Bearer {token}",
            "content-type": "application/json"
        }
        try:
            response = make_post_request(
                f"{settings.url}/{settings.version}/{settings.phone_id}/messages",
                headers=headers, data=json.dumps(data)
            )
            self.message_id = response['messages'][0]['id']

        except Exception as e:
            res = dontmanage.flags.integration_request.json()['error']
            error_message = res.get('Error', res.get("message"))
            dontmanage.get_doc({
                "doctype": "WhatsApp Notification Log",
                "template": "Text Message",
                "meta_data": dontmanage.flags.integration_request.json()
            }).insert(ignore_permissions=True)

            dontmanage.throw(
                msg=error_message,
                title=res.get("error_user_title", "Error")
            )

    def format_number(self, number):
        """Format number."""
        if number.startswith("+"):
            number = number[1:len(number)]

        return number
