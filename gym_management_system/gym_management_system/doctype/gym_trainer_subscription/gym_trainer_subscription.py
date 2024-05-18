# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_days,add_months,add_years


class GymTrainerSubscription(Document):
	def validate(self):
		if self.subscription_plan == "Weekly":
			self.end_date = add_days(self.start_date, 7)
		elif self.subscription_plan == "Monthly":
			self.end_date = add_months(self.start_date, 1)
		elif self.subscription_plan == "Yearly":
			self.end_date = add_years(self.start_date, 1)
