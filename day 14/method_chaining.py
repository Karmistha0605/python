class Burger:
    
    def bun(self):
        print("bun")
        return self
    
    def cheese(self):
        print("cheese")
        return self
    
    def ham(self):
        print("ham")
        return self
    
burger=Burger()

burger.bun()\
    .cheese()\
    .ham()\
    .bun()
    
    
    