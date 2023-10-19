class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, info in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print()

    def search_contact(self, keyword):
        found_contacts = {}
        for name, info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in info['phone']:
                found_contacts[name] = info
        if not found_contacts:
            print("No matching contacts found.")
        else:
            self.view_contacts()

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("New Phone (Press Enter to keep current): ")
            email = input("New Email (Press Enter to keep current): ")
            address = input("New Address (Press Enter to keep current): ")
            contact_manager.update_contact(name, phone, email, address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
