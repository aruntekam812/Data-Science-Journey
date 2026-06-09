class employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}")

class dancer:
    def __init__(self,dance):
        
        self.dance= dance
    def show(self):
        print(f"the dance is {self.dance}")

class combination(dancer,employee):#multiple inherit on this line
    
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance

obj = combination("Arun","new")
obj.show()

