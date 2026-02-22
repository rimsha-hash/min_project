import json

# Load contacts from file (if exists)
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Contact dictionary (loaded from file)
contacts = load_contacts()

def add_contact(name, phone):
    """Adds or updates a contact."""
    contacts[name] = phone
    save_contacts()
    print(f"✅ Contact '{name}' saved successfully!")

def view_contacts():
    """Displays all contacts."""
    if contacts:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("📭 Contact book is empty!")

def search_contact(name):
    """Searches for a contact."""
    phone = contacts.get(name)
    print(f"{name}: {phone}") if phone else print(f"❌ Contact '{name}' not found!")

def delete_contact(name):
    """Deletes a contact."""
    if contacts.pop(name, None):
        save_contacts()
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print(f"❌ Contact '{name}' not found!")

# Main program loop
while True:
    print("\n📒 Contact Book Menu")
    print("1️⃣ Add Contact")
    print("2️⃣ View Contacts")
    print("3️⃣ Search Contact")
    print("4️⃣ Delete Contact")
    print("5️⃣ Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact(input("Enter name: "), input("Enter phone: "))
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact(input("Enter name to search: "))
    elif choice == "4":
        delete_contact(input("Enter name to delete: "))
    elif choice == "5":
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice! Please enter a number from 1 to 5.")
