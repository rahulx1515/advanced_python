class Student:
    def _init_(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display(self):
        return f"Name: {self.name}, Roll No: {self.roll_number}, Course: {self.course}"

class StudentRecords:
    def _init_(self):
        self.students = []

    def add_student(self, name, roll_number, course):
        self.students.append(Student(name, roll_number, course))

    def view_students(self):
        if not self.students:
            return "No student records available."
        return "\n".join(student.display() for student in self.students)

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student.display()
        return "Student not found."

# Menu-driven program
records = StudentRecords()
while True:
    print("\n1. Add Student\n2. View All Students\n3. Search Student by Roll No\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        course = input("Enter course: ")
        records.add_student(name, roll_number, course)
    elif choice == 2:
        print("\nStudent Records:")
        print(records.view_students())
    elif choice == 3:
        search_roll = input("Enter roll number to search: ")
        print(records.search_student(search_roll))
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")