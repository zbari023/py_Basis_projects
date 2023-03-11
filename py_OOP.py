# oop training
class Calculator:  # class
    def __init__(self,name):  # constructor, which alone called
        print(f'welcome {name}')

    def summe(self, i, j):  # method
        print(i + j);


res = Calculator('everyone')
res.summe(2, 8)

'''
# in test
class mobil:
    def __int__(self, Art, color, price):
        self.Art = Art
        self.color = color
        self.price = price


samsung = mobil('s8', 'red', '900')
print(samsung.marka)
'''
'''
# Example 2
class Car:
   # Constructor
   def __init__(self, name, year_built, model):
       self.name = name
       self.year_built = year_built
       self.model = model

   def __repr__(self):
        return f'Car({self.name},{self.year_built},{self.model})'


c1 = Car('minicooper','1970','MX1')
print(c1)
'''
