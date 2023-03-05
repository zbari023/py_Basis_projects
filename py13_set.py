# set
x = {6,5,4,3,2,1,"ziad",(11,12,13)}
y = {99,98,100}
print(type(x))                                # <class 'set'>
print(x | y)                                  # {1, 2, 3, 4, 5, 6, 98, 'ziad', 99, 100, (11, 12, 13)} merge 2 set
y.add(200)
print(y)                                      # {200, 98, 99, 100} add a Element
y.discard(100)
print(y)                                      # {200, 98, 99} remove a Element
y.clear()
print(y)                                      # set() clear all element in set