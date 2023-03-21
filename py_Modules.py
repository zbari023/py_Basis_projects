import os
# to read from file
file = open('test2.txt','r')    # read from file using 'r' or 'r+'
print(file.tell())
words = file.readlines()        # just a special words , a part from file , or readlines for all of file
print(file.tell())              # to know where is the position of mouse
print(words)
file.close()


# to write in file
file2 = open('test1.txt','w')
words2 = file2.write('I am here today\nI am ziad bari')
print(words2)
file2.close()

# to append in file
file3 = open('test1.txt','a')
words3 = file3.write('\nI am here today\nI am ziad bari')  # will be at the end of old file
print(words3)
file3.close()