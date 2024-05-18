# Copyright (c) 2024, Abhishek and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters)
	chart=get_chart_data(data)
	return columns, data,None,chart



def get_columns():
	return [
		{
			"fieldname":"member",
			"label": "Gym Member",
			"fieldtype": "Link",
			"options": "Gym Member",
			"width": 200
		},
		{
			"fieldname":"member_name",
			"label": "Member Name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname":"date",
			"label": "Date",
			"fieldtype": "Date",
			"width": 200
		},
		{
			"fieldname":"weight",
			"label": "Weight In Kg",
			"fieldtype": "Float",
			"width": 200
		},
		{
			"fieldname":"calories_intake",
			"label": "Calories",
			"fieldtype": "Float",
			"width": 200
		},
		{
			"fieldname":"body_fat",
			"label": "Body Fat",
			"fieldtype": "Percent",
			"width": 200
		},
		{
			"fieldname":"exercise_duration",
			"label": "Exercise Duration",
			"fieldtype": "Duration",
			"width": 200
		}
	]


def get_data(filters):
	all_data=[]
	if filters.get("member"):
		doc=frappe.get_doc("Gym Member",filters.get("member"))
		for data in doc.fitness_log:
			all_data.append({
				"member_name":doc.full_name,
				"member":doc.name,
				"weight":data.get("weight"),
				"calories_intake":data.get("calories_intake"),
				"body_fat":data.get("body_fat"),
				"exercise_duration":data.get("exercise_duration"),
				"date":data.get("date")
			})
	return all_data



def get_chart_data(data):
    if data:
        labels = []
        weights = []
        calories_intake = []
        body_fat = []
        exercise_duration = []

        for report_data in data:
            labels.append(report_data["date"])
            weights.append(report_data["weight"])
            calories_intake.append(report_data["calories_intake"])
            body_fat.append(report_data["body_fat"])
            exercise_duration.append(report_data["exercise_duration"])

        chart = {
            "data": {
                "labels": labels,
                "datasets": [
                    {
                        "name": "Weight",
                        "chartType": "line",
                        "values": weights
                    },
                    {
                        "name": "Calories Intake",
                        "chartType": "line",
                        "values": calories_intake
                    },
                    {
                        "name": "Body Fat",
                        "chartType": "line",
                        "values": body_fat
                    },
                    {
                        "name": "Exercise Duration",
                        "chartType": "line",
                        "values": exercise_duration
                    }
                ]
            },
            "type": "line"
        }
        return chart
    else:
        return None				