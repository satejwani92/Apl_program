class Country():
    def __init__(self):
        self.office = "delhi"
class State:
    def __init__(self):
        self.office = 'Mumbai'

class Distict(State,Country):
    def __init__(self,office):
        self.office = office
        print(f'district constructor call {self.office}')

d = Distict('kolhapur')
c = State()
a = Country()
print(d.__dict__)
