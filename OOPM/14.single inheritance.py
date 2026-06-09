class animal():
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread

    def sound(self):
        print(f"{self.name} are mmake sound and it is {self.bread}")

class cat(animal):

    def __init__(self,name,bread,name2): 
        animal.__init__(self,name,bread)
        self.name2 =name2
        
    def bark(self):
        print(f"{self.name2} is barking")

obj1=animal("dog","american")
obj1.sound()

obj2= cat("catt","indian","lion")

obj2.sound()
obj2.bark()
