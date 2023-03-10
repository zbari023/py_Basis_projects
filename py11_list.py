# Listen und ausgeführten Befehle:
nameList = ["ziad" , "Andree" , "stefan" , 7 , 8.3]  # kann veschiedene variabeln enthalten
print(nameList)
print(nameList[-1])  # Egal wie viel Elemente wir haben mit -1 greifen wir den letzten Element
print(nameList[0])  # wird von 0 angefangen um den ersten stelle zu greifen

# add a element in our str
x=[1,3,2,5,4,6,7]
y=[11,12,13,14,15,16]
print(x)           # [1, 2, 3, 4, 5, 6, 7]
x.append(8)
print(x)             # [1, 2, 3, 4, 5, 6, 7, 8]
x.insert(0,0)
print(x)             # [0, 1, 2, 3, 4, 5, 6, 7, 8] insert(position, added element)
x.extend(y)
print(x)             # [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16] 2 list in one
x.sort(reverse=True)
print(x)             # [16, 15, 14, 13, 12, 11, 8, 7, 6, 5, 4, 3, 2, 1, 0] sortiert ab während x.sort() zu
x.remove(16)
print(x)             # [15, 14, 13, 12, 11, 8, 7, 6, 5, 4, 3, 2, 1, 0] remove element

# convert a result to list
j = []
names = ["ziad", "bari", "ibrahim"]
for i in names:
    j.append(len(i))
print(j)                  # [4, 4, 7] convert a result to list