# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import frappe.utils


class GymClass(Document):
	def after_insert(self):
		recipients=frappe.get_all("Gym Member",{"enable":1},"email")
		url=str(frappe.utils.get_url())+"/app/"+"gym-class"+"/"+str(self.name)
		if recipients:
			frappe.sendmail(
				recipients=[x.email for x in recipients],
				subject=f"New Class {self.name} is created now",
				message=f"""<b>Click <a href="{url}">here</a> to visit the page.</b>""",
				reference_doctype=self.doctype,
				reference_name=self.name,
			)
