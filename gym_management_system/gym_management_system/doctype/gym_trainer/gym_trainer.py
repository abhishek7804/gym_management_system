# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymTrainer(Document):
	def validate(self):
		self.full_name=self.first_name + " " + self.last_name if self.last_name else self.first_name
