contacts = {}

while True:
    action = input("Add, View, or Quit? ").lower()
    
    if action == "add":
        name = input("Name: ")
        number = input("Phone Number: ")
        contacts[name] = number
        print(f"Added {name}.")
    
    elif action == "view":
        for name, number in contacts.items():
            print(f"{name}: {number}")
    
    elif action == "quit":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option.")
