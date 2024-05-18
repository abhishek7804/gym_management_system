# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymLockerBooking(Document):
    def on_submit(self):
        self.date_validation()
        self.number_of_locker_validate()
    def date_validation(self):
        if self.start_date:
            if frappe.db.exists(self.doctype, {"docstatus":1,"start_date": ("<=",self.start_date),"end_date": (">=",self.end_date), "name": ("!=", self.name),"locker_number":self.locker_number}):
                frappe.throw(frappe._("Locker is already book for this time period"))
    def number_of_locker_validate(self):
        gym_locker=frappe.db.get_value("Gym Settings","Gym Settings","total_locker")
        if self.locker_number > int(gym_locker):
            frappe.throw(frappe._(f"Only {gym_locker} locker is available in our gym"))