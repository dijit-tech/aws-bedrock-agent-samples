class FacilitiesAccessAgent:
    def __init__(self):
        self.access_card_issued = False
        self.facilities_checklist = []

    def issue_access_card(self, new_hire):
        # Logic to issue access card to the new hire
        self.access_card_issued = True
        return f"Access card issued to {new_hire}."

    def provide_facilities_checklist(self):
        # Logic to provide a checklist of facilities
        self.facilities_checklist = [
            "Main Office - 1st Floor",
            "Break Room - 2nd Floor",
            "Conference Room A - 3rd Floor",
            "Parking Lot Access",
            "Emergency Exits"
        ]
        return self.facilities_checklist

    def onboard_new_hire(self, new_hire):
        access_card_message = self.issue_access_card(new_hire)
        checklist = self.provide_facilities_checklist()
        return {
            "access_card_message": access_card_message,
            "facilities_checklist": checklist
        }