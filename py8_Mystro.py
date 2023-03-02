"""
# in bei if Anweisung
x = [1,2,3,5,1]
if 1 in x:
    print("not")
    if 2 in x:
     print("ok ist da")
    else:
        print("):")

# Wenn die if/else Anweisung in einer Zeile geschrieben Wird
y=6
print(True) if y==6 else print(False)
# all für die (and) Abkurzung ,any für die (or) Abkurzung
z1=2 ;z2=3;z3=4
if all([z1==2 , z2==3 , z3==4]):
    print("ok")
if not (z1==2 and z2==6):
    print(True)
"""
# while loop
x = 0
while x <= 10:
    print(x)
    x = x + 1 ;
else:
    print("end program")
print('++++++++++++++++++')
# for loop
for y in range(0,11,1):
    if y==5:
        continue
    print(y)#
print('++++++++++++++++++')
# Example for loop
print('Number\tsqrt')
print('-----------------')
for n in range(1,11):
    print(n,'\t\t',n*n)
# Exanple 2 , Matrix erstellen in test
row=int(input("Enter number of rows: "))
col=int(input("Enter number of cols: "))
for i in range(row):
    for j in range(col):
        print(,end='')     # end befehl um den untereinander
    print(' ')





