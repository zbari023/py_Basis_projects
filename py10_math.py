# Verkettung num and str
from math import *

# round function
print(round(4.6))  # 5
# floor ,ceil function
print(floor(3.9))  # 3
print(ceil(3.9))   # 4
# pow "Exponent"
print(pow(2,5))
# Betraf
print(abs(-3))
# min and max
print(max(4,5))
print(min(88,100))


# a new calculator using python

print("my new calculator using python")
num1 = float(input("Enter your first Number: "))
operator = input("enter your operator: ")
num2 = float(input("Enter your second Number: "))
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "//":
    print(num1//num2)
elif operator == "^":
    print(pow(num1,num2))
else :
    print("error")


from py_OOP2 import Maximum    # call of class in py_oop2


