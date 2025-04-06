from flask import Flask
from agent_handlers.welcome_agent import WelcomeAgent
from agent_handlers.facilities_agent import FacilitiesAccessAgent
from agent_handlers.tech_assets_agent import TechAssetsProvisioningAgent
from agent_handlers.activities_agent import DailyActivitiesGenerationAgent
from agent_handlers.onboarding_supervisor import OnboardingSupervisor

app = Flask(__name__)

# Initialize agents
welcome_agent = WelcomeAgent()
facilities_agent = FacilitiesAccessAgent()
tech_assets_agent = TechAssetsProvisioningAgent()
activities_agent = DailyActivitiesGenerationAgent()
onboarding_supervisor = OnboardingSupervisor()

@app.route('/start_onboarding/<new_hire_id>', methods=['POST'])
def start_onboarding(new_hire_id):
    onboarding_supervisor.start_onboarding(new_hire_id)
    return {"message": "Onboarding process started for new hire."}, 200

if __name__ == '__main__':
    app.run(debug=True)