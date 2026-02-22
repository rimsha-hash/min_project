#contact book code using dictionary
#dictonary to store contact
contacts={}
def add_contact(name,phone):
    contacts[name]=phone
    print(f"Contact {name} added successsfully")
def view_contacts():
    if not contacts:
        print("contact book is empty")
    else:
        print("\n--Contact list--")
        for name,phone in contacts.items():
            print(f"{name} :{phone}")
def search_contact(name,phone):
    if name in contacts:
        print(f"{name} :{contacts[name]}")
    else:
        print(f"{name} not found in book")
def update_contact(name,new_phone):
    if name in contacts:
        contacts[name]=new_phone
        print(f"{name} updated successfully!")
    else:
        print(f"{name} not found ")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully!")
    else:
        print(f"{name} not found!")
while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Deleted Contact")
    print("6. Exit")
    choice=input("Enter your choicce: ")
    if choice=='1':
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        add_contact(name,phone)
    elif choice=='2':
        view_contacts()
    elif choice=='3':
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        search_contact(name,phone)
    elif choice=='4':
        name=input("Enter name: ")
        new_phone=input("Enter new phone number:")
        update_contact(name,new_phone)
    elif choice=='5':
        name=input("Enter name:")
        delete_contact(name)
    elif choice=='6':
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")