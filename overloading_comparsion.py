class Hotel:
    def __init__(self,name,fare):
        self.name = name
        self.fare = fare
    
    def __gt__(self,other):
        return self.fare > other.fare   
        
h1 = Hotel('taj hotel',20000)
h2 = Hotel('sayaji', 10000)

print(h1<h2)