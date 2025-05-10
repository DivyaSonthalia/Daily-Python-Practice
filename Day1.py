# Student Grade Tracker
# This program helps track student names and their marks with a simple menu interface

def display_menu():
    print("\n--- Student Grade Tracker ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Calculate Average Marks")
    print("4. Find Top Student")
    print("5. Exit")

# Dictionary to store student name and mark
students = {}

# Main Loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        # Add Student
        name = input("Enter student name: ").strip()
        if name in students:
            print(">>Student already exitst. Try another name.")
            continue
        try:
            mark = float(input("Enter Student mark (0-100)"))
            if mark < 0 or mark > 100:
                print("Please enter a valid mark between 0 and 100.")
                continue
            students[name] = mark
            print(f">>Added {name} with mark {mark}.")
        except ValueError:
            print(">>Invalid Mark. Please enter a number.")
        
    elif choice == '2':
        # View All Students
        if not students:
            print(">>No Student records found.")
        else:
            print("\nList of students:")
            for name, mark in students.items():
                print(f">>Name: {name}, Mark: {mark}")

    elif choice == '3':
        # Calculate Average Marks
        if not students:
            print(">>No students to calculate average.")
        else:
            avg = sum(students.values()) / len(students)
            print(f">>Average mark of all students: {avg:.2f}")
    
    elif choice == '4':
        # Find top student
        if not students:
            print(">>No students to compare.")
        else:
            max_mark = max(students.values())
            top_students = [name for name, mark in students.items() if mark == max_mark]
            print(f">>Top marks is {max_mark}, achieved by: {', '.join(top_students)}")
        
    elif choice == '5':
        # Exit
        print(">>Exiting program. Goodbye!")
        break
    
    else:
        print(">>Invalid Choice. Please enter number from 1 to 5.")
    