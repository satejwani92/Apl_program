class Student:
    def __init__(self,name,roll,dd,mm,yy):
        self.name = name
        self.roll = roll
        self.DOB = self.DOB(dd,mm,yy)
    def display(self):
        print(f"name is {self.name} and roll no is {self.roll}")
        self.dob.display()
        
class DOB:
    def __init__(self,dd,mm,yy):
        self.date = dd
        self.month = mm
        self.year = yy
        
    def display(self):
        print(f"date of birth date is {self.date} / {self.month} / {self.year}")
        
s1 = Student('ajay',101,26,3,1999) 
s1.display()           
        