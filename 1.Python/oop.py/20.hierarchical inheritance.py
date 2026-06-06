class supercalss:
    def __init__(self,name1):
        self.name1 =name1

    def show(self):
        print(f"{self.name1} is a hero")
class A1(supercalss):
    def __init__(self,name1,name2):
        super().__init__(name1)
        self.name2=name2
    def show(self):
        super().show()
        print(f"{self.name2} is a villain")

class A2(supercalss):
    def __init__(self,name1,name3):
        super().__init__(name1)
        
        self.name3=name3
    def show(self):
        super().show()
        print(f"{self.name3} is a player")

class B1(A2):
    def __init__(self,name1,name2,name3,name4):
        super().__init__(name1,name3)

        self.name4=name4


    def show(self):
        super().show()
        print(f"{self.name4} is a goat")


obj = B1("arun","raka","scout","mortal")
obj.show()
