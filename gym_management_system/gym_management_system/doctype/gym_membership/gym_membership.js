// Copyright (c) 2024, Abhishek and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership", {
	setup(frm) {
        frm.set_query('subscription_type','locker_details', function(frm,cdt,cdn) {
            return {
                filters:{
                    with_locker:1
                }
            }
        })
        frm.set_query('subscription_type','trainer_subscription', function(frm,cdt,cdn) {
            let item = locals[cdt][cdn];
            if (!item.subscription_plan){
                frappe.throw("Please select Subscription Plan")
            }
            return {
                filters:{
                    with_trainer:1,
                    subscription_plan:item.subscription_plan
                }
            }
        })

	},
});


