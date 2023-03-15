# documentation / files
import os

file = open('test.txt','r')
print(file.tell())
word = file.readlines()
print(file.tell())
print(word)
file.close()
file = open('test.txt','w')
writing = file.write(' i am here')
print(writing)