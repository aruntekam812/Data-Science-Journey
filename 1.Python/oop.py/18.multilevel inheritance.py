class ultrapro:
    def __init__(self,maxx):
        self.maxx=maxx
    def show(self):
        print(f"jonathan is {self.maxx}")

class pro(ultrapro):
    def __init__(self,maxx,low):
        super().__init__(maxx)
        # self.maxx=maxx # we use super() keyword to acess the parent class method/parametere
        self.low=low

    def show(self):
        ultrapro.show(self)
        print(f"scout is {self.low}")

class bot(pro):
    def __init__(self,maxx,low,poor):
        super().__init__(maxx,low)
        # self.maxx=maxx
        # self.low=low
        self.poor=poor

    def show(self):
        pro.show(self)
        print(f"mortal is {self.poor}")


obj1=bot("mvp","mr internation","goat")

obj1.show()

# obj2=bot("universal","mr","noob")
# obj2.show()

