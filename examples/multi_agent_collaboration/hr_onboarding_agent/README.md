# HR Onboarding Agent

The HR Onboarding Agent streamlines the onboarding process for new employees by automating tasks such as sending welcome emails, arranging facilities access, provisioning technology assets, and generating daily activity guides. It uses a set of sub-agents to ensure a smooth and efficient onboarding experience.


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

pip3 install -r requirements.txt
```

1. Deploy HR Onboarding Agents

``` python
python3 main.py --recreate_agents "true"
```

2. Invoke the HR onboarding process
``` python
python3 main.py \
--recreate_agents "false" \
--employee_name "John Smith" \
--job_title "Data Scientist" \
--department "Data Analytics" \
--start_date "2025-06-01"
```

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

The code was generated using Copilot. Below are the prompts:
```
The agents.yaml file gives details of vairous agents involved in a multi agent collaboration for a startup advisor agent. Based on these agents come up with a new agents.yaml file for a multi agent collaboration for an HR onboarding agent for a new hire. Come up with what agents would be requried for the workflow including "welcome agent", "facilities access agent", "tech assets provisioning agent","daily activities generation agent". The daily activities generation agent will look up role descritions by searching the internet and come up with a sample daily tasks for the new hire. Make appropriate assumptions for rest of the agents
```

```
Based on the agents.yaml modify the main.py to create appropriate agents
```

```
update the tasks.yaml based on the agents.yaml and main.py. be as descriptive as possible
```