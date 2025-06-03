import os

RECORDS = "day9_grades.txt"
CREDENTIALS_FILE = "credentials.txt"

class UserAuth:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.credentials = {}
        self.load_credentials()

    def load_credentials(self):
        if os.path.exists(self.credentials_file):
            with open(self.credentials_file, "r") as f:
                for line in f:
                    user, pwd = line.strip().split(',')
                    self.credentials[user] = pwd
    
    def authenticate(self):
        print("Login required")
        for attempt in range(3):
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if self.credentials.get(username) == password:
                print("Login Successful")
                return True
            else:
                print("Invalid Credentials. Try Again!")
        print("Too many Failed attempts. Exiting")
        return False

class Student:
    def __init__(self, name, ID, subject, marks):
        self.name = name.strip()
        self.ID = ID.strip()
        self.subject = subject.strip()
        self.marks = marks.strip()

    def __str__(self):
        return f"Name: {self.name} | ID: {self.ID} | Subject: {self.subject} | Marks: {self.marks}"
    
    def to_line(self):
        return f"{self.name},{self.ID},{self.subject},{self.marks}\n"
    
class GradeBook:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.load_records()

    def load_records(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        student = Student(*parts)
                        self.students.append(student)

    def save_records(self):
        with open(self.filename, "w") as f:
            for student in self.students:
                f.write(student.to_line())

    def add_student(self):
        name = input("Enter Student's Name: ")
        ID = input("Enter student's unique ID: ")
        subject = input("Enter the subject name: ")
        marks = input("Enter the marks for that subject: ")

        if not name or not ID or not subject or not marks:
            print("❌ All fields are required.")
            return

        new_student = Student(name, ID, subject, marks)
        self.students.append(new_student)
        self.save_records()
        print(f"✅ Student '{name}' added successfully.")

    def view_records(self):
        if not self.students:
            print("📁 No records found.")
            return

        print("\n📘 All Records:")
        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. {student}")

    def search_student(self):
        keyword = input("Enter name to search: ").strip().lower()
        found = False
        print("\n🔍 Search Results:")
        for student in self.students:
            if keyword in student.name.lower():
                print(student)
                found = True
        if not found:
            print("No matching record found.")

    def delete_student(self):
        keyword = input("Enter the student ID to delete: ").strip()
        original_count = len(self.students)
        self.students = [s for s in self.students if s.ID != keyword]
        if len(self.students) < original_count:
            self.save_records()
            print(f"🗑️ Student record with ID: {keyword} deleted successfully.")
        else:
            print(f"Student record with ID {keyword} not found.")

    def show_menu(self):
        print("\n--- STUDENT GRADE BOOK SYSTEM ---")
        print("1. Add new student record")
        print("2. View all records")
        print("3. Search student by name")
        print("4. Delete student by ID")
        print("5. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select an option (1-5): ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_records()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                print("👋 Exiting System. Bye!")
                break
            else:
                print("❌ Invalid choice! Please try again.")
            
if __name__ == "__main__":
    auth = UserAuth(CREDENTIALS_FILE)
    if auth.authenticate():
        app = GradeBook(RECORDS)
        app.run()