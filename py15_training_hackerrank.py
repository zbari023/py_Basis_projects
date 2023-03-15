# programm um den Zahlen nebeneinander zu generieren
'''
n=int(input("enter :"))
for x in range(1,n+1,1):
    print(f"{x},",end='')                 # 1,2,3,4,5,6,7,
'''
for m in range(1,101):
    if (m % 2) == 0 and m in range(2,5):
        print(m)
