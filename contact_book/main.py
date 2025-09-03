# Basic CLI-based contact book

contacts = {}

while True:
    action = input("\nChoose an action: Add, View, Search, Delete, or Quit: ").lower()

    if action == "add":
        name = input("Name: ")
        number = input("Phone Number: ")
        contacts[name] = number
        print(f"✅ Added {name}.")

    elif action == "view":
        if contacts:
            print("\n📒 Contact List:")
            for name, number in contacts.items():
                print(f"{name}: {number}")
        else:
            print("No contacts found.")

    elif action == "search":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"🔍 Found: {search_name} - {contacts[search_name]}")
        else:
            print("❌ Contact not found.")

    elif action == "delete":
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"🗑️ Deleted {delete_name}.")
        else:
            print("❌ Contact not found.")

    elif action == "quit":
        print("👋 Goodbye!")
        break

    else:
        print("⚠️ Invalid option. Please choose Add, View, Search, Delete, or Quit.")
