class details:
    name = "arun"
    occupation = "data scientist"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

obj1 = details()
obj2 = details()
obj3= details()

obj2.name = "amit"
obj2.occupation = "engineer"

obj3.name = "ayush"
obj3.occupation = " badmosh boy"

# print(obj1.name,"is a",obj1.occupation)# without using self function 
# print(obj2.name,"is a",obj2.occupation)# without using self function
# print(obj3.name,"is a",obj3.occupation)# without using self function


obj1.info()
obj2.info()
obj3.info()