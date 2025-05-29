import os

RECORDS = "oop_grades.txt"

class Student:
    def __init__(self, name, student_id, subject, marks):
        self.name = name.strip()
        self.student_id = student_id.strip()
        self.subject = subject.strip()
        self.marks = marks.strip()

    def __str__(self):
        return f"{self.name},{self.student_id},{self.subject},{self.marks}"

    def display(self):
        return f"Name: {self.name} | Student ID: {self.student_id} | Subject: {self.subject} | Marks: {self.marks}"
    
class Gradebook:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.load_students()        

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        student = Student(*parts)
                        self.students.append(student)
    
    def save_students(self):
        with open(self.filename, 'w') as f:
            for student in self.students:
                f.write(str(student) + '\n')
    
    def add_student(self):
        name = input("Enter Student's name: ")
        student_id = input("Enter Student ID: ")
        subject = input("Enter Subject: ")
        marks = input("Enter marks: ")

        if not name or not student_id or not subject or not marks:
            print(" All fields are required.")
            return
        
        new_student = Student(name, student_id, subject, marks)
        self.students.append(new_student)
        self.save_students()
        print(f"Student'{name}' added successfully.")

    def view_all(self):
        if not self.students:
            print("No records to display.")
            return
        print("\n All Records:")
        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. {student.display()}")

    def search_student(self):
        keyword = input("Enter name to search: ").strip().lower()
        found = False
        print("\n Search Results: ")
        for student in self.students:
            if keyword in student.name.lower():
                print(student.display())
                found = True
            if not found:
                print("No matching record found.")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ").strip()
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < initial_count:
            self.save_students()
            print(f" Student with ID {student_id} deleted successfully")
        else:
            print(f"No student found with ID {student_id}.")

def main():
    gradebook = Gradebook(RECORDS)

    while True:
        print("\n--- STUDENT GRADE BOOK SYSTEM ---")
        print("1. Add new student record")
        print("2. View all records")
        print("3. Search student by name")
        print("4. Delete student by ID")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()
        if choice == '1':
            gradebook.add_student()
        elif choice == '2':
            gradebook.view_all()
        elif choice == '3':
            gradebook.search_student()
        elif choice == '4':
            gradebook.delete_student()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()