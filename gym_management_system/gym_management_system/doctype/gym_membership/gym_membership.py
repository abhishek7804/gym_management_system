# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe.utils import flt



class GymMembership(Document):
	def validate(self):
		if self.end_date < nowdate():
			self.is_active=0
		if self.locker_details:
			self.total_locker_amount()
		if self.trainer_subscription:
			self.total_trainer_subscription_amount()
		self.set_default_membership_amount()
		self.grand_total=flt(self.membership_amount)+flt(self.locker_amount)+flt(self.trainer_subscription_amount)
	def on_submit(self):
		if self.locker_details:
			self.locker_creation()
		if self.trainer_subscription:
			self.create_trainer_subscritption()
		
	def locker_creation(self):
		for locker_data in self.locker_details:
			frappe.get_doc({
				"doctype":"Gym Locker Booking",
				"member":self.member,
				"locker_number":locker_data.get("locker"),
				"start_date":locker_data.get("start_date"),
				"end_date":locker_data.get("end_date"),
				"amount":locker_data.get("amount"),
				"membership":self.name
			}).save().submit()
	def create_trainer_subscritption(self):
		for subscritption_data in self.trainer_subscription:
			frappe.get_doc({
					"doctype":"Gym Trainer Subscription",
					"trainer":self.trainer,
					"subscription_plan":subscritption_data.get("subscription_plan"),
					"start_date":subscritption_data.get("start_date"),
					"rating":subscritption_data.get("rating"),
					"amount":subscritption_data.get("amount"),
				}).save().submit()
	def set_default_membership_amount(self):
		basic_amount,premium_amount,other_amount=frappe.db.get_value("Gym Settings","Gym Settings",["basic_membership_amount","premium_membership_amount","basic_membership_amount"])
		if self.membership_type=="Basic":
			self.membership_amount=basic_amount
		elif self.membership_type=="Premium":
			self.membership_amount=premium_amount
		else:
			self.membership_amount=other_amount
	def total_locker_amount(self):
		self.locker_amount=sum([x.get("amount") for x in self.locker_details])
	def total_trainer_subscription_amount(self):
		self.trainer_subscription_amount=sum([x.get("amount") for x in self.trainer_subscription])				
            

def check_active_membership():
    over_due_memebership_list=frappe.get_all("Gym Membership",{"docstatus":1,"is_active":1,"end_date": ("<",nowdate())})
    for data in over_due_memebership_list:
        frappe.db.set_value("Gym Membership",data.name,"is_active",0)