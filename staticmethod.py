class Bank:
    bank_name = 'BOI'
    rate_of_interest = 12.25
    @staticmethod
    def Simple_interest(prin,n):
        si = (prin*n*Bank.rate_of_interest)/100
        print(si)
        
prin = float(input("enter the principal"))
n = int(input("enter the no of years"))
Bank.Simple_interest(prin,n)
