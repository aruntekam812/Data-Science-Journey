class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"the name is {self.name} and id is {self.id}")
#inherit start
class programer(employee):
    def showlanguage(self):
        print("the language is python")


obj1 = employee("Arun",400)
obj2 = employee("arjun",500)
obj3=programer("ankit",200) #programmer inherit the employee details

obj1.showdetails()
obj2.showdetails()
obj3.showdetails()
obj3.showlanguage()