class Employee:
    dept_location = "Chicago"
    def __init__(self,aname,asalary,adept) -> None:
        self.name=aname
        self.salary = asalary
        self.dept= adept
    
    def printDetails(self):
        print(f"The name is {self.name}, The salary is {self.salary}, The dept location is {self.dept_location}")

    @classmethod
    def changeLocation(cls, newdept_location):
        cls.dept_location=newdept_location


azaan = Employee("Azaan",100000000000, "CEO")
mahi = Employee("Mahi", 432340, "Teacher")

azaan.changeLocation("Los Angeles")
mahi.printDetails()


# def dec1(func1):
#     def nowExec(a,b):
#         print("Executing")
#         func1(a,b)
#         print("Executed")
#     return nowExec

# @dec1
# def sum1(a,b):
#     print(a+b)

# sum1(10213,3102)