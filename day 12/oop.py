class House:
    colour="red"
    garden=True
    windows=10
    
    def set_colour(self,colour):
        self.colour=colour
    
my_house=House()
print(my_house.colour)

house_2=House()
print(my_house.colour)

house_2.set_colour("green")
print(type(house_2.colour))

