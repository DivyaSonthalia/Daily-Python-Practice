# Simple Student Management System
# Features Covered - Modular Design Using Functions, File operations, List & Dict, Type Casting, Error Handling

import os

# Global Constants
FILENAME = "students_day3.txt"

# Student list where each student is a dictionary
students = []

# Function to load students from a file
def load_students():
    if not os.path.exists(FILENAME):
        return
    
    with open(FILENAME, "r") as files:
        for line in files:
            parts = line.strip().split("::")
            if len(parts) == 3:
                name, roll, marks = parts
                students.append({
                    "name" : name,
                    "roll" : roll,
                    "marks" : float(marks)
                })
            
# Function to save students as file
def save_students():
    with open(FILENAME, "w") as file:
        for student in students:
            file.write(f"{student['name']}::{student['roll']}::{student['marks']}\n")

# Function to display name
def show_menu():
    print("--- Student Management System ---")
    print("1. Add student")
    print("2. View All students")
    print("3. Search student by roll number")
    print("4. Delete student by roll number")
    print("5. Save students to file.")
    print("6. Exit")

# Function to add a student
def add_student():
    name = input("Enter student's name: ").strip()
    roll = input("Enter student's roll number: ").strip()
    try:
        marks = float(input("Enter Student's Marks: "))
    except ValueError:
        print("Invalid input for marks.")
        return
    
    for s in students:
        if s["roll"] == roll:
            print("Student with this roll number already exists.")
            return
        
    students.append({
        "name" : name,
        "roll" : roll,
        "marks" : marks
    })
    print("Student added successfully.")

# Function to view all students.
def view_students():
    if not students:
        print("No students found.")
        return
    
    print("\n--- Student list ---")
    for s in students:
        print(f"Name: {s['name']}, Roll No.: {s['roll']}, Marks: {s['marks']}")
    
# Function to search a student by roll number
def search_students():
    roll = input("Enter roll number to search: ").strip()
    for s in students:
        if s['roll'] == roll:
            print(f"Found: Name: {s['name']}, Roll No.: {s['roll']}, Marks: {s['marks']}")
            return
    print("student not found.")

# Function to delete a student by roll number
def del_students():
    roll = input("Enter roll number to delete: ").strip()
    for i, s  in enumerate(students):
        if s['roll'] == roll:
            del students[i]
            print("student deleted successfully.")
            return
    print("student not found.")

# Main Driver function
def main():
    load_students()
    while True:
        show_menu()
        choice = input("Enter your choice(1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_students()
        elif choice == '4':
            del_students()
        elif choice == '5':
            save_students()
            print("Student saved to file.")
        elif choice == '6':
            save_students()
            print("Exiting.. Students saved.")
            break
        else:
            print("Invalid Choice. Please try again.")
        
# Entry Point
if __name__ == "__main__":
    main()
