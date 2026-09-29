import json
import os

# File where contacts are stored so they are not lost when the program closes
FILE_NAME = "contacts.json"


def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Search Contacts")
    print("7. Exit")


def load_contacts():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # keep the damaged file as a backup so it is not overwritten
        os.replace(FILE_NAME, FILE_NAME + ".bak")
        print("Contacts file was damaged. Starting fresh (old file saved as .bak).")
        return {}
    except OSError:
        print("Could not read the contacts file. Starting with an empty book.")
        return {}


def save_contacts(contact_book):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(contact_book, f, indent=4)
    except OSError:
        print("Error: could not save contacts to file.")


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]


def add_contact(contact_book):
    name = input("Enter name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return
    if name in contact_book:
        print("Contact already exists!")
        return

    phone = input("Enter phone (10 digits): ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number! It must have exactly 10 digits.")
        return

    email = input("Enter email (optional): ").strip()
    if email != "" and not is_valid_email(email):
        print("Invalid email address!")
        return

    address = input("Enter address (optional): ").strip()
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contact_book)
    print("Contact added successfully!")


def view_contact(contact_book):
    name = input("Enter name to view: ").strip()
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")


def edit_contact(contact_book):
    name = input("Enter name to edit: ").strip()
    if name in contact_book:
        print("Leave a field blank to keep the current value.")
        phone = input("New phone: ").strip()
        email = input("New email: ").strip()
        address = input("New address: ").strip()

        if phone == '':
            phone = contact_book[name]['phone']
        elif not is_valid_phone(phone):
            print("Invalid phone number! Contact not updated.")
            return

        if email == '':
            email = contact_book[name]['email']
        elif not is_valid_email(email):
            print("Invalid email address! Contact not updated.")
            return

        if address == '':
            address = contact_book[name]['address']

        contact_book[name] = {"phone": phone, "email": email, "address": address}
        save_contacts(contact_book)
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact(contact_book):
    name = input("Enter name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        save_contacts(contact_book)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        # sorted so the list is always in alphabetical order
        for name in sorted(contact_book, key=str.lower):
            details = contact_book[name]
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()  # Blank line between contacts for readability


def search_contacts(contact_book):
    keyword = input("Enter name or part of a name to search: ").strip().lower()
    if keyword == "":
        print("Search text cannot be empty!")
        return
    found = False
    for name, details in contact_book.items():
        if keyword in name.lower():
            print(f"Name: {name} | Phone: {details['phone']}")
            found = True
    if not found:
        print("No matching contacts found.")


def main():
    # Contact book dictionary (loaded from the file)
    contact_book = load_contacts()

    # Main loop
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contact(contact_book)
        elif choice == "3":
            edit_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            list_all_contacts(contact_book)
        elif choice == "6":
            search_contacts(contact_book)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
