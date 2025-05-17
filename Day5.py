# SIMPLE CONTACT BOOK
# BUILDING A SIMPLE CLI_BASED CONTACT BOOK USING PYTHON

import os 

# FIle to store contact data
CONTACT_FILE = "DAY5_contacts.txt"

# Function to display menu
def show_menu():
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add new contact")
    print("2. View All contacts")
    print("3. Search contact by name")
    print("4. Delete contact")
    print("5. Exit")

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact number: ").strip()
    email = input("Enter contact Email id: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return
    
    with open(CONTACT_FILE,"a") as f:
        f.write(f"{name},{phone},{email}\n")
    print(f"Contact '{name}' added successfully.")

# Function to view all contacts
def view_contacts():
    if not os.path.exists(CONTACT_FILE):
        print("No contacts found yet.")
        return
    
    with open(CONTACT_FILE,"r") as f:
        lines = f.readlines()
    
    if not lines:
        print("Contact book is empty.")
        return
    
    print("\n All contacts:")
    for idx, line in enumerate(lines, start=1):
        name, phone, email = line.strip().split(',')
        print(f"{idx}. Name: {name} | Phone: {phone} | Email: {email}")
    
# Function to search contact by name
def search_contact():
    keyword = input("Enter name to search: ").strip().lower()

    if not os.path.exists(CONTACT_FILE):
        print("No contacts to search.")
        return
    
    found = False
    with open(CONTACT_FILE,'r') as f:
        for line in f:
            name, phone, email = line.strip().split(',')
            if keyword in name.lower():
                print(f"Found: Name: {name} | Phone: {phone} | Email: {email}")
                found = True
            
    if not found:
        print("No matching contact found.")
    
# Function to delete contact
def delete_contact():
    keyword = input("Enter the exact name of the contact to delete: ").strip()

    if not os.path.exists(CONTACT_FILE):
        print("No contacts to delete.")
        return
    
    updated_lines = []
    deleted = False
    with open(CONTACT_FILE,'r') as f:
        lines = f.readlines()
        for line in lines:
            name, phone, email = line.strip().split(',')
            if name != keyword:
                updated_lines.append(line)
            else:
                deleted = True

    if deleted:
        with open(CONTACT_FILE,'w') as f:
            f.writelines(updated_lines)
        print(f"Contact with name: {keyword} deleted successfully.")
    else:
        print(f"Contact with name {keyword} not found")

# Main application
def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("👋 Exiting Contact Book. Bye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Entry point

if __name__ == "__main__":
    main()