# oop training
class Calculator:  # class
    def __init__(self, name):  # constructor, which alone called # encapsulation with self
        print(f'welcome {name}')

    def summe(self, i, j):  # method
        print(i + j);


class Scical(Calculator):  # inheritance
    def multi(self, i, j):
        print(i * j)


erg = Scical('Bari')
erg.summe(45, 7)



# Example 1

class Mobil:
    def __init__(self, Art, price):
        self.Art = Art
        self.price = price
    def show(self):
        print(self.Art + " is neu!")
        print(f"{self.price} is good price!")

c1 = Mobil('S8', '1200')
c1.show()

# Example 2
class Car:
   
   def __init__(self, name, year_built, model):           # Constructor
       self.name = name
       self.year_built = year_built
       self.model = model

   def show(self):
         print(f'Car({self.name},{self.year_built},{self.model})')

c2 = Car('minicooper','1970','MX1')
c2.show()

'''
# Result:
welcome Bari
52
S8 is neu!
1200 is good price!
Car(minicooper,1970,MX1)
'''