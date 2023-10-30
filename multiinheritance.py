class Employee:
    company = 'visa'
    score = 120

class Freelancer:
    company = 'fiverr'
    level = 0
    def upgradescore(self):
        self.level = self.level + 1
        
class Programmer(Employee,Freelancer):
    name = 'rohit'

c = Programmer()
c.upgradescore()
print(c.level)
c = Freelancer()
print(c.company)
c = Employee()
print(c.company)
c = Programmer()
print(c.name)
