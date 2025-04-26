# contact_book.py

from storage import load_contacts, save_contacts

def add_contact(name, phone, email):
    contacts = load_contacts()
    if name in contacts:
        print(" Contact already exists.")
        return
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(" Contact added successfully.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Contact list is empty.")
        return
    print("\n Contact List:")
    for name, info in contacts.items():
        print(f"- {name}:  {info['phone']}, {info['email']}")

def edit_contact(name):
    contacts = load_contacts()
    if name not in contacts:
        print(" Contact not found.")
        return
    phone = input("Enter new phone number: ")
    email = input("Enter new email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(" Contact updated successfully.")

def delete_contact(name):
    contacts = load_contacts()
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    save_contacts(contacts)
    print("Contact deleted successfully.")
