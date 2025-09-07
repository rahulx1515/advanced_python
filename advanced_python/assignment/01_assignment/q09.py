class Employee:
    def _init_(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Designation: {self.designation}, Salary: ${self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary
        return f"Salary updated to ${new_salary}"

    def promote(self, new_designation):
        self.designation = new_designation
        return f"Promoted to {new_designation}"

# Menu-driven program
employees = []
while True:
    print("\n1. Add Employee\n2. View All Employees\n3. Update Salary\n4. Promote Employee\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter employee name: ")
        designation = input("Enter designation: ")
        salary = float(input("Enter salary: "))
        employees.append(Employee(name, designation, salary))
    elif choice == 2:
        if not employees:
            print("No employees available.")
        else:
            for emp in employees:
                print(emp.display_info())
    elif choice in [3, 4]:
        name = input("Enter employee name: ")
        emp = next((e for e in employees if e.name == name), None)
        if emp:
            if choice == 3:
                new_salary = float(input("Enter new salary: "))
                print(emp.update_salary(new_salary))
            else:
                new_designation = input("Enter new designation: ")
                print(emp.promote(new_designation))
        else:
            print("Employee not found.")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")