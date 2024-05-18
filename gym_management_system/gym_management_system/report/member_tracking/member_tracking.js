// Copyright (c) 2024, Abhishek and contributors
// For license information, please see license.txt

frappe.query_reports["Member Tracking"] = {
	"filters": [
		{
			"fieldname":"member",
			"label": __("Gym Member"),
			"fieldtype": "Link",
			"options": "Gym Member",
			"reqd": 1
		}

	]
};
