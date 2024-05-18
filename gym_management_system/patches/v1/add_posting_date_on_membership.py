import frappe
def execute():
    try:
        frappe.db.sql("""
            UPDATE `tabGym Membership`
            SET posting_date = start_date
            WHERE posting_date IS NULL
        """)

        frappe.db.commit()
    except Exception as e:
        frappe.db.rollback()
        print(e)