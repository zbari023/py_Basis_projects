# documentation / files
import os

file = open('test.txt','r')
print(file.tell())
word = file.readlines()
print(file.tell())
print(word)
file.close()
# file = open('test.txt','w')
file = open('test.txt','a')
writing = file.write(' \n i am here and \n My name is ziad Bari from syria')
print(writing)
print(file.tell())
file.close()