class Employee:
    company = 'Google'
    
    def showclass(self):
        print('it an employee')
    
class programmer(Employee):
    langauge = 'python'
    #company = 'youtube'  # overriding 
    def getlangauge(self):
        print(f"the lang is {self.langauge}")
    def showclass(self):
        print('this is an employee class') 
        
        
e = Employee()
e.showclass()
p = programmer()
#print(p.company) #overriding
p.showclass()