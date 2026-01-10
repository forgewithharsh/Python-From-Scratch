class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)


e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 3000)
# print(Employee.company)
e1.print_info()
e2.print_info()