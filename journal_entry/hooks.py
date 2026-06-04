app_name = "journal_entry"
app_title = "Journal Entry GCG"
app_publisher = "Aan Kristian Sitinjak"
app_description = "Aplikasi kustomisasi jurnal"
app_email = "kristiansitinjak270@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "journal_entry",
# 		"logo": "/assets/journal_entry/logo.png",
# 		"title": "Journal Entry GCG",
# 		"route": "/journal_entry",
# 		"has_permission": "journal_entry.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/journal_entry/css/journal_entry.css"
# app_include_js = "/assets/journal_entry/js/journal_entry.js"

# include js, css files in header of web template
# web_include_css = "/assets/journal_entry/css/journal_entry.css"
# web_include_js = "/assets/journal_entry/js/journal_entry.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "journal_entry/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "journal_entry/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "journal_entry.utils.jinja_methods",
# 	"filters": "journal_entry.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "journal_entry.install.before_install"
# after_install = "journal_entry.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "journal_entry.uninstall.before_uninstall"
# after_uninstall = "journal_entry.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "journal_entry.utils.before_app_install"
# after_app_install = "journal_entry.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "journal_entry.utils.before_app_uninstall"
# after_app_uninstall = "journal_entry.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "journal_entry.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "journal_entry.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"journal_entry.tasks.all"
# 	],
# 	"daily": [
# 		"journal_entry.tasks.daily"
# 	],
# 	"hourly": [
# 		"journal_entry.tasks.hourly"
# 	],
# 	"weekly": [
# 		"journal_entry.tasks.weekly"
# 	],
# 	"monthly": [
# 		"journal_entry.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "journal_entry.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "journal_entry.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "journal_entry.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "journal_entry.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["journal_entry.utils.before_request"]
# after_request = ["journal_entry.utils.after_request"]

# Job Events
# ----------
# before_job = ["journal_entry.utils.before_job"]
# after_job = ["journal_entry.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"journal_entry.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

