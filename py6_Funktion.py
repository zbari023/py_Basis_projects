# einfache Funktion erstellen:
def say_hello():
    print("Hallo Welt")
    print("Ich bin ein Funktion")


say_hello()


# Beispiel:


def mysum(i=0, j=0):
    return i + j
ressum = mysum(32)
print(ressum)

def mysub(i, j):
    return i - j
ressub = mysub(32, 8)
print(ressub)

def mymult(i, j):
    return i * j
resmult = mymult(32, 8)
print(resmult)


def mydiv(i, j):
    return i / j
resdiv = mydiv(32, 8)
print(resdiv)

listN = [ressum, ressub, resmult, resdiv]
print(listN)


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


