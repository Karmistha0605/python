class Grandfather:
    def __init__(self):
        print("Grandfather has a luxurious House")
        
    house="luxury house"
    
class Father(Grandfather):
    def __init__(self):
        print("Father has a 3 floor house")
        
    car="ferrari"

class Mother:
    jewellery="diamond"
    
class Son(Father):
    def __init__(self):
        print("Son had bought 2 houses")
        super().__init__() #displays the class of the before class
        
    electronics="PS5"
    
    
son= Son()

father=Father()

print(isinstance(son,Mother))#if object belongs in a class
#print(son.car)
#print(son.jewellery)
#print(son.house)



