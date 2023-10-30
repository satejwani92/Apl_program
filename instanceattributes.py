class Employee:
    company = "google"
    salary = 100
vijay = Employee()
sara = Employee() 
#vijay.salary = 300  #in instance it will seen where another name of salary is their like wise it will cheack.
#if their is no such instancr attribute it will check in class.and it will print.
#sara.salary = 400
print(vijay.company)
print(sara.company)
print(vijay.salary)
print(sara.salary)