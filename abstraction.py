from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def good(self):
        print("all car has the 100 kmph")
    def colour(self):
        print("white")

class Maruti_Suzuki(Car):
    def good(self):
        print("Mileage is 40 kmph")
        
class TATA(Car):
    def good(self):
        print("Mileage is 30 kmph")
        
class Honda(Car):
    def good(self):
        print("Mileage is 70 kmph")
        
        
m1 = Maruti_Suzuki()
t1 = TATA()
h1 = Honda()
h1.good()
t1.good()
m1.good()
h1.colour()
h1.good()