import unittest
from src.agent_handlers.welcome_agent import WelcomeAgent

class TestWelcomeAgent(unittest.TestCase):

    def setUp(self):
        self.agent = WelcomeAgent()

    def test_send_welcome_email(self):
        new_hire_email = "new_hire@example.com"
        result = self.agent.send_welcome_email(new_hire_email)
        self.assertTrue(result)
        self.assertIn("Welcome", self.agent.last_email_subject)
        self.assertIn("We are excited to have you", self.agent.last_email_body)

    def test_provide_onboarding_info(self):
        onboarding_info = self.agent.provide_onboarding_info()
        self.assertIsInstance(onboarding_info, dict)
        self.assertIn("welcome_message", onboarding_info)
        self.assertIn("resources", onboarding_info)

if __name__ == '__main__':
    unittest.main()