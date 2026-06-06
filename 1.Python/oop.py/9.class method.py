class employee:
    company = "apple"
     
    def show(self):
        
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def change(self,newcompany):
       self.company=  newcompany
 
obj = employee()
obj.name = "arun"
obj.show()
obj.change("Tesla")
obj.show()
print(employee.company)

