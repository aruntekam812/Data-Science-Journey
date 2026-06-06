class employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary = salary

    def show(self):
        print(f"the name is {self.name} and salary is {self.salary}")

    @classmethod
    def bgmi(self,string):
        return self(string.split("-")[0],string.split("-")[1])
    
  
obj= employee("Arun", 500000)
# print(obj.name)
# print(obj.salary)
obj.show()#using self function



string="john-2000"
obj1=employee.bgmi(string)
# print(obj1.name)
# print(obj1.salary)
obj1.show()#using self function