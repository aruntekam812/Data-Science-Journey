class person:
    def __init__(self,n,o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a  {self.occ}")
         
a= person("Abhay","enginner")
b= person("Ankush","machanical enginner")
a.info()
b.info()
      

