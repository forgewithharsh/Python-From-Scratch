class Employee:
    company = "HP"

    def get_salary(self): # self is important here because self is a way to reference the object of the class which is being created
        return 34000
    

e1 = Employee() # An Object of class Employee is created here
print(e1.get_salary()) # Employee's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)