import unittest
from src.agent_handlers.tech_assets_agent import TechAssetsAgent

class TestTechAssetsAgent(unittest.TestCase):

    def setUp(self):
        self.agent = TechAssetsAgent()

    def test_provision_laptop(self):
        result = self.agent.provision_laptop("new_hire@example.com")
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], "Laptop provisioned successfully.")

    def test_provision_software_access(self):
        result = self.agent.provision_software_access("new_hire@example.com", ["email", "slack"])
        self.assertTrue(result['success'])
        self.assertIn("Software access granted for: email, slack", result['message'])

    def test_provision_accessories(self):
        result = self.agent.provision_accessories("new_hire@example.com", ["mouse", "keyboard"])
        self.assertTrue(result['success'])
        self.assertIn("Accessories provisioned: mouse, keyboard", result['message'])

    def test_invalid_email(self):
        result = self.agent.provision_laptop("invalid_email")
        self.assertFalse(result['success'])
        self.assertEqual(result['message'], "Invalid email address.")

if __name__ == '__main__':
    unittest.main()