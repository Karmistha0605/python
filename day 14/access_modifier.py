class Person:
    def __init__(self):
        #public
        self.name = "Som"
        #private
        self._age = "20" 
        #proctected
        self.__phone_number="9807465783" 
    
    @property
    def phone_number(self):
        return self.__phone_number 
    
    @phone_number.setter
    def phone_number(self,phone_number):
        self.__phone_number = phone_number
        

    
p=Person()

p.phone_number="12231221"
print(p.phone_number)

#p.set_number("9801231231")

#print(p.get_number())

#print(p.get_number())

#p.name="Radha"

#print(p.name)

