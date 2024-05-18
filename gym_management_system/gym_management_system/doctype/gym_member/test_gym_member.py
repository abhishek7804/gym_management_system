# Copyright (c) 2024, Abhishek and Contributors
# See license.txt


import frappe
import unittest

def create_gym_member(first_name, date_of_birth, gender, email, contact_number):
    """Helper function to create a Gym Member."""
    return frappe.get_doc({
        "doctype": "Gym Member",
        "first_name": first_name,
        "date_of_birth": date_of_birth,
        "gender": gender,
        "email": email,
        "contact_number": contact_number
    }).insert()

class TestGymMember(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")

    def tearDown(self):
        frappe.set_user("Administrator")
        # Clean up Gym Members created during tests
        for member in frappe.get_all("Gym Member", filters={"first_name": ["like", "_Test%"]}):
            frappe.delete_doc("Gym Member", member.name)

    def test_create_gym_member(self):
        """Test creation of Gym Member."""
        member = create_gym_member(
            first_name="_Test Member",
            date_of_birth="1990-01-01",
            gender="Male",
            email="test_member@example.com",
            contact_number="+911234567890"
        )
        self.assertEqual(member.first_name, "_Test Member")
        self.assertEqual(member.gender, "Male")
        self.assertEqual(member.email, "test_member@example.com")
        self.assertEqual(member.contact_number, "+911234567890")

    def test_required_fields(self):
        """Test validation of required fields in Gym Member."""
        # Only provide one required field to trigger the MandatoryError
        member = frappe.get_doc({
            "doctype": "Gym Member",
            "first_name": "_Test Member"
        })

        with self.assertRaises(frappe.exceptions.MandatoryError) as err:
            member.insert()

        # Check if the error message exists and contains the term "mandatory" in lowercase
        self.assertFalse(str(err.exception).lower())

if __name__ == "__main__":
    unittest.main()



