class employee:
    def __init__(self,name , id):
        self.name = name
        self.id = id

    def show(self):
            print(f"the name is {self.name} or id is {self.id}")

class programer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

    def show2(self):
        print(f"lang is {self.lang}")

obj=employee("arun",1)
obj.show()
obj1=programer("viksit", "500", "python")
obj1.show()
obj1.show2()