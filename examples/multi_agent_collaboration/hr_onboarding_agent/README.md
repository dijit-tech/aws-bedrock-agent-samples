# HR Onboarding Agent

The HR Onboarding Agent streamlines the onboarding process for new employees by automating tasks such as sending welcome emails, arranging facilities access, provisioning technology assets, and generating daily activity guides. It uses a set of sub-agents to ensure a smooth and efficient onboarding experience.

![architecture](/images/architecture.gif)

## Features

The HR Onboarding Agent consists of the following sub-agents:

1. **Welcome Agent**: Sends a personalized welcome email to the new hire, including onboarding instructions and company resources.
2. **Facilities Access Agent**: Manages physical access requirements such as building access cards, office space allocation, and parking permits.
3. **Tech Assets Provisioning Agent**: Provisions all necessary technology assets, including hardware, software, and system access.
4. **Daily Activities Generation Agent**: Generates a sample list of daily activities and responsibilities for the new hire based on their role.
5. **Onboarding Supervisor**: Oversees the entire onboarding process, ensuring all tasks are completed and consolidated into a comprehensive onboarding package.

## Prerequisites

1. Clone and install the repository:

```bash
git clone https://github.com/awslabs/amazon-bedrock-agent-samples

cd amazon-bedrock-agent-samples

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r [requirements.txt](http://_vscodecontentref_/1)

1. Deploy HR Onboarding Agents

python3 main.py --recreate_agents "true"

2. Invoke the HR onboarding process

python3 main.py \
--recreate_agents "false" \
--employee_name "John Smith" \
--job_title "Data Scientist" \
--department "Data Analytics" \
--start_date "2025-06-01"

Tasks Overview
The HR Onboarding Agent performs the following tasks:

Welcome Task:

Sends a personalized welcome email with onboarding details.
Saves the email and employee details in the agent store.
Facilities Task:

Arranges physical access requirements such as building access cards and office space.
Saves the facilities access plan and checklist in the agent store.
Tech Assets Task:

Provisions hardware, software, and system access for the new hire.
Saves the technology provision plan and setup instructions in the agent store.
Daily Activities Task:

Generates a sample list of daily activities and responsibilities for the new hire.
Saves the daily activities guide and a "first 30 days" plan in the agent store.
Onboarding Completion Task:

Compiles all onboarding information into a comprehensive onboarding package.
Saves the onboarding package and a manager's checklist in the agent store.
License
This project is licensed under the Apache-2.0 License.