class Student:
    def _init_(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        avg_marks = sum(self.marks) / len(self.marks)
        if avg_marks >= 80:
            return "A"
        elif avg_marks >= 60:
            return "B"
        elif avg_marks >= 40:
            return "C"
        else:
            return "F"

students = []
while True:
    print("\n1. Add Student\n2. View Grades\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = list(map(int, input("Enter marks in 3 subjects separated by space: ").split()))
        students.append(Student(name, roll_number, marks))
    elif choice == 2:
        for student in students:
            print(f"{student.name} ({student.roll_number}) - Grade: {student.calculate_grade()}")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")