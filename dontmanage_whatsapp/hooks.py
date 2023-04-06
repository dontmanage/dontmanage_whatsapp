from . import __version__ as app_version

app_name = "dontmanage_whatsapp"
app_title = "DontManage Whatsapp"
app_publisher = "Shridhar Patil"
app_description = "WhatsApp integration for dontmanage"
app_email = "shridhar.p@zerodha.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dontmanage_whatsapp/css/dontmanage_whatsapp.css"
# app_include_js = "/assets/dontmanage_whatsapp/js/dontmanage_whatsapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/dontmanage_whatsapp/css/dontmanage_whatsapp.css"
# web_include_js = "/assets/dontmanage_whatsapp/js/dontmanage_whatsapp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dontmanage_whatsapp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#   "Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#   "methods": "dontmanage_whatsapp.utils.jinja_methods",
#   "filters": "dontmanage_whatsapp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dontmanage_whatsapp.install.before_install"
# after_install = "dontmanage_whatsapp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dontmanage_whatsapp.uninstall.before_uninstall"
# after_uninstall = "dontmanage_whatsapp.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See dontmanage.core.notifications.get_notification_config

# notification_config = "dontmanage_whatsapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#   "Event": "dontmanage.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#   "Event": "dontmanage.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#   "ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#   "*": {
#       "on_update": "method",
#       "on_cancel": "method",
#       "on_trash": "method"
#   }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#   "all": [
#       "dontmanage_whatsapp.tasks.all"
#   ],
#   "daily": [
#       "dontmanage_whatsapp.tasks.daily"
#   ],
#   "hourly": [
#       "dontmanage_whatsapp.tasks.hourly"
#   ],
#   "weekly": [
#       "dontmanage_whatsapp.tasks.weekly"
#   ],
#   "monthly": [
#       "dontmanage_whatsapp.tasks.monthly"
#   ],
# }

# Testing
# -------

# before_tests = "dontmanage_whatsapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#   "dontmanage.desk.doctype.event.event.get_events": "dontmanage_whatsapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other DontManage apps
# override_doctype_dashboards = {
#   "Task": "dontmanage_whatsapp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#   {
#       "doctype": "{doctype_1}",
#       "filter_by": "{filter_by}",
#       "redact_fields": ["{field_1}", "{field_2}"],
#       "partial": 1,
#   },
#   {
#       "doctype": "{doctype_2}",
#       "filter_by": "{filter_by}",
#       "partial": 1,
#   },
#   {
#       "doctype": "{doctype_3}",
#       "strict": False,
#   },
#   {
#       "doctype": "{doctype_4}"
#   }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#   "dontmanage_whatsapp.auth.validate"
# ]


doc_events = {
    "*": {
        "before_insert": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "after_insert": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "before_validate": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "validate": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "on_update": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "before_submit": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "on_submit": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "before_cancel": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "on_cancel": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "on_trash": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "after_delete": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "before_update_after_submit": "dontmanage_whatsapp.utils.run_server_script_for_doc_event",
        "on_update_after_submit": "dontmanage_whatsapp.utils.run_server_script_for_doc_event"
    }
}
