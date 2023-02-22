# einfache Funktion erstellen:
# Programm ,der gibt, welche Zahl größer ist
def say_hello():
    print("Hallo Welt")
    print("Ich bin ein Funktion")
say_hello()

# eine Funktion mit Parameter: Beispeil:
def maximum(x, y):
    if x > y:
        return x                   # immer in einer Funktion muss ein Wert zurückgegeben mit return
    elif x == y:
        return print("sind gleich")
    else:
        return y
res = maximum(4, 100)              # Aufrufen des Funktion im Code
print(res)