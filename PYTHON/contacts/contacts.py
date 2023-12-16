import json
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)

def display_contacts(contacts):
    a = "error"
    if not contacts:
        print("No contacts found.")
        return a
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def add_contact(contacts, name, phone, email, address):
    try:
        phone = int(phone)
    except ValueError:
        print("Error! Enter only digits for the phone number.")
        return

    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    print("Contact added successfully.")


def search_contact(contacts, search_term):
    results = [contact for contact in contacts if
               search_term.lower() in contact['name'].lower() or str(search_term) == str(contact['phone'])]
    return results


def update_contact(contacts, index, name, phone, email, address):
    contacts[index] = {'name': name, 'phone': phone, 'email': email, 'address': address}
    save_contacts(contacts)
    print("Contact updated successfully.")

def delete_contact(contacts, index):
    if not contacts:
        print("Contact list is empty. Nothing to delete.")
        return
    try:
        deleted_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact '{deleted_contact['name']}' deleted successfully.")
    except IndexError:
        print("Invalid contact index.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. View Contact List")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            name = input("Enter name: ")
            try:
              phone = int(input("Enter phone number: "))
            except:
                print("Error! Enter only digits")
                continue
            email = input("Enter email address:(optional) ")
            address = input("Enter address:(optinal) ")
            add_contact(contacts, name, phone, email, address)
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_results = search_contact(contacts, search_term)
            display_contacts(search_results)
        elif choice == '4':
            display_contacts(contacts)
            try:
                index = int(input("Enter the index of the contact to update: ")) - 1
                if 0 <= index < len(contacts):
                    name = input("Enter new name: ")
                    phone = input("Enter new phone number: ")
                    email = input("Enter new email address:(optional) ")
                    address = input("Enter new address:(optional) ")
                    update_contact(contacts, index, name, phone, email, address)
                else:
                    print("Invalid contact index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            a = display_contacts(contacts)
            if(a == "error"):
                continue
            try:
                index = int(input("Enter the index of the contact to delete: ")) - 1
                if 0 <= index < len(contacts):
                    delete_contact(contacts, index)
                else:
                    print("Invalid contact index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '6':
            print("Quitting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
