import frappe
from frappe import _
from datetime import datetime

@frappe.whitelist()
def get_profile_data(member_id):
    member = frappe.get_doc("Gym Member", {"email": member_id})

    # Get active plan
    active_plan = frappe.get_doc("Gym Membership", {"member": member.name, "is_active": 1})

    # Ensure active_plan is retrieved correctly
    if active_plan:
        end_date = active_plan.end_date
        now_date = datetime.strptime(frappe.utils.nowdate(), '%Y-%m-%d').date()

        # Calculate remaining days
        remaining_days = (end_date - now_date).days
    else:
        remaining_days = 0


    # Get past plans
    past_plans = frappe.get_all("Gym Membership", filters={"member": member.name, "is_active": 0}, fields=["name", "start_date", "end_date"])
    allocated_trainer = frappe.get_doc("Gym Trainer",active_plan.trainer)
    return {
        "member": member,
        "active_plan": active_plan.name,
        "remaining_days": remaining_days,
        "allocated_trainer": allocated_trainer,
        "past_plans": past_plans
    }
