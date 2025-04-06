class OnboardingSupervisor:
    def __init__(self, agents):
        self.agents = agents

    def oversee_onboarding(self, new_hire):
        self.send_welcome_email(new_hire)
        self.provision_facilities_access(new_hire)
        self.provision_tech_assets(new_hire)
        self.generate_daily_activities(new_hire)

    def send_welcome_email(self, new_hire):
        welcome_agent = self.agents.get('welcome_agent')
        welcome_agent.send_email(new_hire)

    def provision_facilities_access(self, new_hire):
        facilities_agent = self.agents.get('facilities_agent')
        facilities_agent.provide_access(new_hire)

    def provision_tech_assets(self, new_hire):
        tech_assets_agent = self.agents.get('tech_assets_agent')
        tech_assets_agent.provision_assets(new_hire)

    def generate_daily_activities(self, new_hire):
        activities_agent = self.agents.get('activities_agent')
        activities_agent.generate_tasks(new_hire)