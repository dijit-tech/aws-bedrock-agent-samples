class TechAssetsAgent:
    def __init__(self):
        self.assets = []

    def provision_assets(self, new_hire_info):
        # Logic to provision tech assets based on the new hire's role
        self.assets.append("Laptop")
        self.assets.append("Software Access")
        self.assets.append("Other Equipment")
        return self.assets

    def send_confirmation(self, new_hire_email):
        # Logic to send a confirmation email to the new hire
        confirmation_message = f"Tech assets provisioned: {', '.join(self.assets)}"
        # Code to send email (not implemented here)
        return confirmation_message

    def get_assets(self):
        return self.assets