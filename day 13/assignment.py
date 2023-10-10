#inheritance program.
class Animal:
    def __init__(self) -> None:
        print("There are 2 kinds of animals")
    types="Domestic"    

class Dog(Animal):
    def __init__(self):
        print("My name is browny")
    colour="brown"          

labrador = Dog()
print(labrador)
print(labrador.colour)






