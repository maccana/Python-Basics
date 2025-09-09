class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, number in self.contacts.items():
                print(f"{name}: {number}")

    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} deleted.")
        else:
            print("Contact not found.")

# CLI interface
book = ContactBook()

while True:
    action = input("\nChoose: Add, View, Search, Delete, Quit: ").lower()

    if action == "add":
        name = input("Name: ")
        number = input("Phone: ")
        book.add_contact(name, number)

    elif action == "view":
        book.view_contacts()

    elif action == "search":
        name = input("Search name: ")
        print(book.search_contact(name))

    elif action == "delete":
        name = input("Delete name: ")
        book.delete_contact(name)

    elif action == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
