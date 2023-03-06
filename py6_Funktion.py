# einfache Funktion erstellen:
def say_hello():
    print("Hallo Welt")
    print("Ich bin ein Funktion")


say_hello()


# Beispiel:
def mycalc(i, j):
    print("mysum is : ", i + j)
    print("mydiv is : ", i - j)
    print("mymult is : ", i * j)
    return print("mydiff is : ", i / j)
mycalc(10,5)
'''
return must be at the end line of the function order
mysum is :  15
mydiv is :  5
mymult is :  50
mydiff is :  2.
'''

# eine Funktion mit Parameter: Beispeil:
# Programm ,der gibt, welche Zahl größer ist
def maximum(x, y):
    if x > y:
        return x  # immer in einer Funktion muss ein Wert zurückgegeben mit return
    elif x == y:
        return print("sind gleich")
    else:
        return y


res = maximum(9, 100)  # Aufrufen des Funktion im Code
print(res)
