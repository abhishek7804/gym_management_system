# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class SubscriptionType(WebsiteGenerator,Document):
	pass
