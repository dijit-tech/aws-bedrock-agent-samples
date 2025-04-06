import unittest
from src.agent_handlers.facilities_agent import FacilitiesAccessAgent

class TestFacilitiesAccessAgent(unittest.TestCase):

    def setUp(self):
        self.agent = FacilitiesAccessAgent()

    def test_access_card_issuance(self):
        new_hire = "John Doe"
        result = self.agent.issue_access_card(new_hire)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], f"Access card issued to {new_hire}.")

    def test_facilities_checklist(self):
        checklist = self.agent.get_facilities_checklist()
        self.assertIn("Main Office", checklist)
        self.assertIn("Break Room", checklist)
        self.assertIn("Emergency Exits", checklist)

    def test_facilities_access_info(self):
        access_info = self.agent.get_access_info()
        self.assertIsInstance(access_info, dict)
        self.assertIn("access_hours", access_info)
        self.assertIn("contact_person", access_info)

if __name__ == '__main__':
    unittest.main()