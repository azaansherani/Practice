class Student():
    def __init__(self, name, age, standard):
        self.name = name
        self.age = age
        self.standard = standard

    def printStudents(self):
        print(self.name, self.age, self.standard)

class Student2(Student):
    def __init__(self, name, age, standard, address, phno):

        super().__init__(name, age, standard)
        self.address = address
        self.phno = phno

class Student3(Student):
    def __init__(self, name, age, standard, teachername):
        super().__init__(name, age, standard)
        self.teachername = teachername
    
    
    def printStudents(self):
        print(self.teachername)

studentlist = [Student("Azaan", 21, 6), Student2("Sakshi",24,6,"Hazaribag",9320902),
                Student3("Roshan",21,7,"Mohini")]

for st in studentlist:
    st.printStudents()
    