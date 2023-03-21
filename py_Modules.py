import os
# to read from file
file = open('test2.txt','r')    # read from file using 'r' or 'r+'
print(file.tell())
words = file.readlines()        # just a special words , a part from file , or readlines for all of file
print(file.tell())              # to know where is the position of mouse
print(words)



# to write in file
file2 = open('test1.txt','w')
words2 = file2.write('I am here today\nI am ziad bari')
file2.close()