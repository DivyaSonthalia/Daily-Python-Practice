# Student Grade Book System
import os

RECORDS = "Day6_grades.txt"

# Function to display menu options
def show_menu():
    print("\n--- STUDENT GRADE BOOK SYSTEM ---")
    print("1. Add new student record")
    print("2. View All records")
    print("3. Search student by name")
    print("4. Delete student by name")
    print("5. Exit")

# Function to add a student record
def add_student():
    name = input("Enter Student's Name: ").strip()
    ID = input("Enter student's unique ID: ").strip()
    subject = input("Enter the subject name: ")
    marks = input("Enter the marks for that subject: ").strip()

    if not name or not ID or not subject or not marks:
        print("Name, ID, subject, marks all fields are required.")
        return
    
    with open(RECORDS,"a") as f:
        f.write(f"{name},{ID},{subject},{marks}\n")
    print(f"Student '{name}' added successfully.")

# Function to view all contacts
def view_records():
    if not os.path.exists(RECORDS):
        print("No records found yet.")
        return
    
    with open(RECORDS,"r") as f:
        lines = f.readlines()
    
    if not lines:
        print("Records are empty.")
        return
    
    print("\n All Records:")
    for idx, line in enumerate(lines, start=1):
        name, ID, subject, marks = line.strip().split(',')
        print(f"{idx}. Name: {name} | ID: {ID} | Subject: {subject} | Marks: {marks}")

# Function to search student by name
def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    if not os.path.exists(RECORDS):
        print("No records to search.")
        return
    
    found = False
    with open(RECORDS,'r') as f:
        for line in f:
            name, ID, subject, marks = line.strip().split(',')
            if keyword in name.lower():
                print(f"Found: Name: {name} | ID: {ID} | Subject: {subject} | Marks: {marks}")
                found = True
            
    if not found:
        print("No matching record found.")

# Function to delete a Student record
def delete_student():
    keyword = input("Enter the exact name of the student to delete: ").strip()

    if not os.path.exists(RECORDS):
        print("No records to delete.")
        return
    
    updated_lines = []
    deleted = False
    with open(RECORDS,'r') as f:
        lines = f.readlines()
        for line in lines:
            name, ID, subject, marks = line.strip().split(',')
            if name != keyword:
                updated_lines.append(line)
            else:
                deleted = True

    if deleted:
        with open(RECORDS,'w') as f:
            f.writelines(updated_lines)
        print(f"Student record with name: {keyword} deleted successfully.")
    else:
        print(f"Student record with name {keyword} not found")

# Main application
def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_records()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting System. Bye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Entry point

if __name__ == "__main__":
    main()