import json
from datetime import date

# Function to add to JSON
class write_value():
    """Writes the value to a JSON file."""
    def __init__(self): 
        self.date = date.today()
        self.formatted_date = self.date.strftime("%d/%m/%Y")

    def write_json(self, data, filename='policies.json'):
        """The function to add the data to the JSON file."""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def open_json(self):
        """Opening the file to append the values."""
        with open('policies.json') as f:
            policies = json.load(f)

            temp = policies['applied_policies']

            new_policy = {
                "policy": "deny acces control panel",
                "comment": "only admins should be able to edit settings",
                "admin": "dieter",
                "GPO": "GPOPFAfdelingen",
                "date": self.formatted_date
                }

        # Appending temp to policies
            temp.append(new_policy)

        write_json(policies)