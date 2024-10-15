import json

class ContactsManager:
    """
    Manages contacts, stored in a JSON file for persistence.
    """
    def __init__(self, file_name='contacts.json'):
        self.file_name = file_name
        self.contacts = self.load_from_file()

    def add_contact(self, name: str, email: str, preferred_time: str = "08:00 AM"):
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)
        self.save_to_file()

    def remove_contact(self, name: str):
        self.contacts = [c for c in self.contacts if c['name'] != name]
        self.save_to_file()

    def get_contacts(self):
        return self.contacts

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")

    def save_to_file(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.contacts, file)

    def load_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
