class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public
        self._project = "Secret"  # Protected
        self.__salary = salary # Private
        
    def show(self):
        print(F"the name is {self.name} or project is {self._project} and the salary is {self.__salary}")
        

emp = Employee("Alice", 5000)
emp.show()





