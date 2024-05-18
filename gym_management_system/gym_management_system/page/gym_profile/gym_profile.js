frappe.pages['gym-profile'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Profile',
        single_column: true
    });

    // Get the member ID (you can get this from the logged-in user's linked member profile)
    const member_id = frappe.session.user;

    // Fetch profile data with member_id argument
    frappe.call({
        method: 'gym_management_system.gym_management_system.page.gym_profile.gym_profile.get_profile_data',
        args: { member_id: member_id },  // Pass member_id argument here
        callback: function(r) {
            if (r.message) {
                renderProfileData(r.message);
            }
        }
    });

    // Function to render profile data
    function renderProfileData(profile) {
        var profileHTML = `
            <h2>${profile.member.first_name} ${profile.member.last_name}</h2>
            <p><strong>Active Plan:</strong> ${profile.active_plan}</p>
            <p><strong>Remaining Days:</strong> ${profile.remaining_days}</p>
			<p><strong>Allocated Trainer:</strong> ${profile.allocated_trainer.name} (Email:${profile.allocated_trainer.email}, Phone:${profile.allocated_trainer.phone_number})</p>
            <h3>Past Plans</h3>
            <ul>
                ${profile.past_plans && profile.past_plans.length > 0 ? 
                    profile.past_plans.map(plan => `<li>${plan.name} (from ${plan.start_date} to ${plan.end_date})</li>`).join('') : 
                    '<li>No past plans found</li>'
                }
            </ul>
        `;
        
        $(page.body).html(profileHTML);
    }
};
