# Copyright (c) 2024, Abhishek and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymMembership(FrappeTestCase):
	def setUp(self):
		# Set up any necessary data here
		pass

	def tearDown(self):
		# Clean up after tests
		pass

	def test_create_gym_membership(self):
		gym_membership = frappe.get_doc({
			"doctype": "Gym Membership",
			"member": "Abhishek-05-2024-00001",
			"start_date": "2024-05-17",
			"posting_date": "2024-05-17",
			"end_date":"2024-05-18",
			"membership_type": "Basic"
		})
		gym_membership.insert()
		
		self.assertTrue(gym_membership.name)
		self.assertEqual(gym_membership.member, "Abhishek-05-2024-00001")
	def test_membership_amount_validation(self):
		gym_membership = frappe.get_doc({
			"doctype": "Gym Membership",
			"member": "test_member",
			"member_name": "Test Member",
			"start_date":"2024-05-17",
			"end_date":"2024-05-17",
			"posting_date": "2024-05-17",
			"membership_amount": -50.00  # Invalid amount for the purpose of this test
		})
		
		with self.assertRaises(frappe.ValidationError):
			gym_membership.insert()	

	if __name__ == '__main__':
		unittest.main()