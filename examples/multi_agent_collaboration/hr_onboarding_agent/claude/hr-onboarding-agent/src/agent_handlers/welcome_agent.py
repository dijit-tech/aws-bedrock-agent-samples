class WelcomeAgent:
    def __init__(self, email_service, template_service):
        self.email_service = email_service
        self.template_service = template_service

    def send_welcome_email(self, new_hire_email, new_hire_name):
        subject = "Welcome to the Team!"
        body = self.template_service.render_welcome_email(new_hire_name)
        self.email_service.send_email(new_hire_email, subject, body)

    def provide_onboarding_info(self, new_hire_name):
        onboarding_info = {
            "welcome_message": f"Welcome {new_hire_name}! We're excited to have you on board.",
            "next_steps": [
                "Complete your employee profile.",
                "Attend the orientation session.",
                "Meet your team members."
            ]
        }
        return onboarding_info

# Example usage:
# email_service = EmailService()  # This would be your email sending service
# template_service = TemplateService()  # This would handle rendering email templates
# welcome_agent = WelcomeAgent(email_service, template_service)
# welcome_agent.send_welcome_email("newhire@example.com", "John Doe")