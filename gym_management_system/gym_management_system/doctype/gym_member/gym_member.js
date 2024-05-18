// Copyright (c) 2024, Abhishek and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Member", {
	setup(frm) {
        frm.set_query('membership', function() {
            return {
                filters:{
                    is_active:1,
                    docstatus:1,
                    member:frm.doc.name
                }
            }
        })
	},
});
