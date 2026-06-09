class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def area(self):
        
        return self.x + self.y
    

class circle(shape):
    def __init__(self,multi):
        self.multi=multi
        super().__init__(multi,multi)

    def  area(self):
        return 3.14 * super().area()

a =shape(5,5)
print(a.area())
obj = circle(5)
print(obj.area())

