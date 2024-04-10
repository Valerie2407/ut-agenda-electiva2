class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})

    def get_contacts(self):
        return self.contacts

    def update_contact(self, name, new_phone):
        for contact in self.contacts:
            if contact["name"] == name:
                contact["phone"] = new_phone
                return True
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact["name"] == name:
                del self.contacts[i]
                return True
        return False