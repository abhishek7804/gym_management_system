# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	return [
		{
			"fieldname":"voucher_type",
			"label": "Voucher Type",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname":"voucher_id",
			"label": "Voucher Id",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname":"amount",
			"label": "Total",
			"fieldtype": "Currency",
			"width": 200
		}
	]


def get_data(filters):
    if filters.get("from_date") and filters.get("to_date"):
        sql_query = """
            SELECT 'Gym Membership' AS voucher_type, name as voucher_id, posting_date, membership_amount AS amount
            FROM `tabGym Membership`
            WHERE docstatus =1 AND posting_date >= '{from_date}' AND posting_date <= '{to_date}' GROUP BY name
            UNION ALL
            SELECT 'Gym Trainer Subscription' AS voucher_type, name as voucher_id, start_date AS posting_date, amount
            FROM `tabGym Trainer Subscription`
            WHERE docstatus =1 AND start_date >= '{from_date}' AND start_date <= '{to_date}' GROUP BY name
            UNION ALL
            SELECT 'Gym Locker Booking' AS voucher_type, name as voucher_id, start_date AS posting_date, amount
            FROM `tabGym Locker Booking`
            WHERE docstatus =1 AND start_date >= '{from_date}' AND start_date <= '{to_date}' GROUP BY name
        """.format(from_date=filters.get("from_date"), to_date=filters.get("to_date"))
        data = frappe.db.sql(sql_query, as_dict=True)
        return data

			  

