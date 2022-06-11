incentives = 1000000
class Employee:
    dept_location = "Chicago"
    def __init__(self,aname,asalary,ajob) -> None:
        self.name=aname
        self.salary = asalary
        self.job= ajob
    
    def printDetails(self):
        global incentives
        print(f"The name is {self.name}, The salary is {self.salary}, The amount of incentives are {incentives}")
        incentives = incentives*213 +212
        print(f"The name is {self.name}, The salary is {self.salary}, The amount of incentives are {incentives}")

    @classmethod
    def changeLocation(cls, newdept_location):
        cls.dept_location=newdept_location


azaan = Employee("Azaan",100000000000, "CEO")
mahi = Employee("Mahi", 432340, "Teacher")

azaan.changeLocation("Los Angeles")
mahi.printDetails()


