class supercalss:
    def __init__(self,name):
        self.name =name

    def show(self):
        print(f"{self.name} is a hero")
class A1(supercalss):
    def __init__(self,name,name2):
        super().__init__(name)
        self.name2=name2
    def show(self):
        print(f"{self.name2} is a villain")

class A2(supercalss):
    def __init__(self,name,name2,name3):
        super().__init__(name,name2)
        self.name3=name3
    def show(self):
        print(f"{self.name3} is a player")

class B1(A1,A2):
    def __init__(self,name,name2,name3):
        self.name=name
        self.name2=name2
        self.name3=name3

obj =   B1("arun","raka","scout")
obj.show()


