import unittest
from src.agent_handlers.activities_agent import DailyActivitiesGenerationAgent

class TestDailyActivitiesGenerationAgent(unittest.TestCase):

    def setUp(self):
        self.agent = DailyActivitiesGenerationAgent()

    def test_generate_daily_tasks(self):
        role_description = "Software Engineer"
        expected_tasks = [
            "Attend daily stand-up meetings",
            "Work on assigned tickets in the project management tool",
            "Participate in code reviews",
            "Collaborate with team members on project features",
            "Test and debug code"
        ]
        generated_tasks = self.agent.generate_daily_tasks(role_description)
        self.assertEqual(generated_tasks, expected_tasks)

    def test_invalid_role_description(self):
        role_description = ""
        with self.assertRaises(ValueError):
            self.agent.generate_daily_tasks(role_description)

    def test_generate_daily_tasks_for_nonexistent_role(self):
        role_description = "Nonexistent Role"
        generated_tasks = self.agent.generate_daily_tasks(role_description)
        self.assertEqual(generated_tasks, [])

if __name__ == '__main__':
    unittest.main()