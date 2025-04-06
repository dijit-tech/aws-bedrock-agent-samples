# HR Onboarding Agent

This project is designed to facilitate the onboarding process for new hires through a multi-agent collaboration system. Each agent is responsible for specific tasks that contribute to a smooth and efficient onboarding experience.

## Project Structure

- **agents.yaml**: Defines the various agents involved in the HR onboarding process, including their roles, goals, and instructions.
  
- **src/**: Contains the implementation of the agents and supporting utilities.
  - **agent_handlers/**: 
    - `welcome_agent.py`: Sends a welcome email and provides initial onboarding information.
    - `facilities_agent.py`: Manages access to physical facilities and provides a checklist.
    - `tech_assets_agent.py`: Provisions necessary tech assets for the new hire.
    - `activities_agent.py`: Generates a sample list of daily tasks based on role descriptions.
    - `onboarding_supervisor.py`: Oversees the entire onboarding process.
  - **utils/**:
    - `store_utils.py`: Utility functions for managing a key-value store.
    - `api_connectors.py`: Functions for connecting to external APIs.
  - **templates/**:
    - `welcome_email.md`: Template for the welcome email.
    - `facilities_checklist.md`: Template for the facilities checklist.
    - `onboarding_plan.md`: Template for the overall onboarding plan.
  - `app.py`: Main entry point for the application.

- **config/**: Contains configuration files.
  - `settings.json`: Configuration settings for the application.
  - `llm_config.json`: Configurations for language models used by the agents.

- **tests/**: Contains unit tests for each agent to ensure functionality and performance.
  - `test_welcome_agent.py`
  - `test_facilities_agent.py`
  - `test_tech_assets_agent.py`
  - `test_activities_agent.py`

- **requirements.txt**: Lists the dependencies required for the project.

## Getting Started

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd hr-onboarding-agent
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```
   python src/app.py
   ```

## Agents Overview

- **Welcome Agent**: Responsible for sending a welcome email and providing initial onboarding information to the new hire.
  
- **Facilities Access Agent**: Manages access to physical facilities, including issuing access cards and providing a checklist of facilities.

- **Tech Assets Provisioning Agent**: Provisions necessary tech assets such as laptops and software access.

- **Daily Activities Generation Agent**: Generates a sample list of daily tasks based on role descriptions found online.

- **Onboarding Supervisor**: Oversees the entire onboarding process, ensuring that all agents are functioning correctly.

## Contribution

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.