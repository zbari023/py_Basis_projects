import os
os.mkdir('New_folder')
writing = open('test10.txt','w')
writing = file.write(' \n i am here and \n My name is ziad Ibrahim Bari from syria, 27, student, married')
print(writing)
print(writing.tell())
writing.close()