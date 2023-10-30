class company:
    company_name = 'infosis' #class variable
    def __init__(self,nm,sal):
        self.name = nm
        self.salary = sal
    @classmethod  
    def get_company_name(cls):
         print(f'company name is',cls.company_name)
        


e1 = company("jay",5000)
e2 = company("vijay",7000)            
company.get_company_name()