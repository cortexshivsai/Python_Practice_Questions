contacts = {}

while True:
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name and phone:
            contacts[name] = phone
            print("Contact saved.")
        else:
            print("Name and phone cannot be empty.")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ").strip()

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice.")