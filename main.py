# main.py

from contact_book import add_contact, view_contacts, edit_contact, delete_contact

def show_menu():
    print("\n Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to edit: ")
            edit_contact(name)

        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)

        elif choice == '5':
            print(" Exiting Contact Manager. Bye!")
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
