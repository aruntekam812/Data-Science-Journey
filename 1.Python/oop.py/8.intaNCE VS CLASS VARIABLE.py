class employee:
    companyName = "apple"
    noofemployees = 0

    def __init__(self,name):
        self.name= name
        self.salary = 1
        employee.noofemployees += 1

    def show(self):
        print(f"the name is {self.name} or salary is {self.salary} and or count {self.noofemployees} company name is {self.companyName}  ")

obj1= employee("arun")
obj1.salary = 2
obj1.companyName= "samsung"
obj2=employee("ayush")
obj2.salary = 5
obj3=employee("ankit")
obj3.salary = 8


obj1.show()
obj2.show()
obj3.show()