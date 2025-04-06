#!/usr/bin/env python

# Copyright 2024 Amazon.com and its affiliates; all rights reserved.
# This file is AWS Content and may not be duplicated or distributed without permission
import sys
from pathlib import Path
import datetime
import traceback
import yaml
import uuid
from textwrap import dedent
import os
import argparse
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from src.utils.bedrock_agent import Agent, SupervisorAgent, Task, region, account_id

current_dir = os.path.dirname(os.path.abspath(__file__))
task_yaml_path = os.path.join(current_dir, "tasks.yaml")
agent_yaml_path = os.path.join(current_dir, "agents.yaml")

def main(args):

    if args.recreate_agents == "false":
        Agent.set_force_recreate_default(False)
    else:
        Agent.set_force_recreate_default(True)
        Agent.delete_by_name("onboarding_supervisor", verbose=True)
    
    if args.clean_up == "true":
        Agent.delete_by_name("onboarding_supervisor", verbose=True)
        Agent.delete_by_name("welcome_agent", verbose=True)
        Agent.delete_by_name("facilities_access_agent", verbose=True)
        Agent.delete_by_name("tech_assets_provisioning_agent", verbose=True)
        Agent.delete_by_name("daily_activities_generation_agent", verbose=True)
        exit()
    else:
        inputs = {
            'employee_name': args.employee_name,
            'job_title': args.job_title,
            'department': args.department,
            'start_date': args.start_date,
        }    

    with open(task_yaml_path, 'r') as file:
        task_yaml_content = yaml.safe_load(file)

        welcome_task = Task('welcome_task', task_yaml_content, inputs)
        facilities_task = Task('facilities_task', task_yaml_content, inputs)
        tech_assets_task = Task('tech_assets_task', task_yaml_content, inputs)
        daily_activities_task = Task('daily_activities_task', task_yaml_content, inputs)
        onboarding_completion_task = Task('onboarding_completion_task', task_yaml_content, inputs)


        web_search_tool = {
            "code":f"arn:aws:lambda:{region}:{account_id}:function:web_search",
            "definition":{
                "name": "web_search",
                "description": "Searches the web for information",
                "parameters": {
                    "search_query": {
                        "description": "The query to search the web with",
                        "type": "string",
                        "required": True,
                    },
                    "target_website": {
                        "description": "The specific website to search including its domain name. If not provided, the most relevant website will be used",
                        "type": "string",
                        "required": False,
                    },
                    "topic": {
                        "description": "The topic being searched. 'news' or 'general'. Helps narrow the search when news is the focus.",
                        "type": "string",
                        "required": False,
                    },
                    "days": {
                        "description": "The number of days of history to search. Helps when looking for recent events or news.",
                        "type": "string",
                        "required": False,
                    },
                },
            },
        }

        set_value_for_key = {
            "code":f"arn:aws:lambda:{region}:{account_id}:function:working_memory",
            "definition":{
                "name": "set_value_for_key",
                "description": " Stores a key-value pair in a DynamoDB table. Creates the table if it doesn't exist.",
                "parameters": {
                    "key": {
                        "description": "The name of the key to store the value under.",
                        "type": "string",
                        "required": True,
                    },
                    "value": {
                        "description": "The value to store for that key name.",
                        "type": "string",
                        "required": True,
                    },
                    "table_name": {
                        "description": "The name of the DynamoDB table to use for storage.",
                        "type": "string",
                        "required": True,
                    }
                },
            },
        }

        get_key_value = {
            "code":f"arn:aws:lambda:{region}:{account_id}:function:working_memory",
            "definition":{
                "name": "get_key_value",
                "description": "Retrieves a value for a given key name from a DynamoDB table.",
                "parameters": {
                    "key": {
                        "description": "The name of the key to store the value under.",
                        "type": "string",
                        "required": True,
                    },
                    "table_name": {
                        "description": "The name of the DynamoDB table to use for storage.",
                        "type": "string",
                        "required": True,
                    }
                },
            },
        }

        with open(agent_yaml_path, 'r') as file:
            agent_yaml_content = yaml.safe_load(file)

        welcome_agent = Agent('welcome_agent', agent_yaml_content,
                            tools=[web_search_tool, set_value_for_key, get_key_value])
        facilities_access_agent = Agent('facilities_access_agent', agent_yaml_content,
                                tools=[web_search_tool, set_value_for_key, get_key_value])
        tech_assets_provisioning_agent = Agent('tech_assets_provisioning_agent', agent_yaml_content,
                                tools=[web_search_tool, set_value_for_key, get_key_value])
        daily_activities_generation_agent = Agent('daily_activities_generation_agent', agent_yaml_content,
                                tools=[web_search_tool, set_value_for_key, get_key_value])
        
        print("\n\nCreating onboarding_supervisor as a supervisor agent...\n\n")
        onboarding_supervisor = SupervisorAgent("onboarding_supervisor", agent_yaml_content,
                                [welcome_agent, facilities_access_agent, 
                                tech_assets_provisioning_agent, daily_activities_generation_agent], 
                                verbose=False)
        
        if args.recreate_agents == "false":
            print("\n\nInvoking supervisor agent...\n\n")

            time_before_call = datetime.datetime.now()
            print(f"time before call: {time_before_call}\n")
            try:
                folder_name = "onboarding-" + str(uuid.uuid4())
                result = onboarding_supervisor.invoke_with_tasks([
                                welcome_task, facilities_task, 
                                tech_assets_task, daily_activities_task,
                                onboarding_completion_task
                            ],
                            additional_instructions=dedent(f"""
                                Use a single Working Memory table for this entire set of tasks, with 
                                table name: {folder_name}. Tell your collaborators this table name as part of 
                                every request, so that they are not confused and they share state effectively.
                                The keys they use in that table will allow them to keep track of any number 
                                of state items they require. When you have completed all tasks, summarize 
                                your work, and share the table name so that all the results can be used and 
                                analyzed."""),
                            processing_type="sequential", 
                            enable_trace=True, trace_level=args.trace_level,
                            verbose=True)
                print(result)
            except Exception as e:
                print(e)
                traceback.print_exc()
                pass

            duration = datetime.datetime.now() - time_before_call
            print(f"\nTime taken: {duration.total_seconds():,.1f} seconds")
        else:
            print("Recreated agents.")
        


if __name__ == '__main__':

    default_inputs = {
        'employee_name': 'Jane Doe',
        'job_title': 'Software Engineer',
        'department': 'Engineering',
        'start_date': '2025-05-01',
    }    

    parser = argparse.ArgumentParser()

    parser.add_argument("--recreate_agents", required=False, default='true', help="False if reusing existing agents.")
    parser.add_argument("--employee_name", required=False, 
                        default=default_inputs['employee_name'],
                        help="The name of the new employee")
    parser.add_argument("--job_title", required=False, 
                        default=default_inputs['job_title'],
                        help="The job title of the new employee")
    parser.add_argument("--department", required=False, 
                        default=default_inputs['department'],
                        help="The department the new employee will join")
    parser.add_argument("--start_date", required=False, 
                        default=default_inputs['start_date'],
                        help="The start date for the new employee")
    parser.add_argument("--trace_level", required=False, default="core", help="The level of trace, 'core', 'outline', 'all'.")
    parser.add_argument(
        "--clean_up",
        required=False,
        default="false",
        help="Cleanup all infrastructure.",
    )
    args = parser.parse_args()
    main(args)