class Employee:
    def _init_(self, name, department, age=30):
        self.name = name
        self.department = department
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Department: {self.department}, Age: {self.age}"

emp1 = Employee("Alice", "HR", 25)  
emp2 = Employee("Bob", "IT")       

print(emp1.display_info())
print(emp2.display_info())