# CLASS METHODS
# class methods can change class variables 
class Employee:
    company_name = "apple"
    def show(self):
        print(f"{self.name} works in {self.company_name}")
    def changeCompany(self, newName):
        self.company_name = newName
a = Employee()
a.name = "habiba"
a.show()
a.changeCompany("tesla")
a.show()
b = Employee()
b.name = "hunain"
b.show() # prints hunain works in apple
# company name gets changed for only object a, not for b
# to change for b as well
print("USING CLASS METHOD")
class Employee2:
    company_name = "apple"
    def show(self):
        print(f"{self.name} works in {self.company_name}")
    @classmethod
    def changeCompany(cls, newName):
        cls.company_name = newName
c = Employee2()
c.name = "habiba"
c.show() # habiba works in apple
c.changeCompany("tesla")
c.show() # habiba works in tesla
d = Employee2()
d.name = "hunain"
d.show() # hunain works in tesla
c.show() # habiba works in tesla



