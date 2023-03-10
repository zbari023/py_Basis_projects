# a program to allow the user to enter his name and password
password = "12345678"  # the right password
user = "zbari"         # the right username
in_user = None         # variabel definition
in_password = None
count=0               # the counter "Zähler"
limit=2                # the max limit "Grenze der Versuche"
condition=False        # condition to stop the while loop after if
while in_user != user and in_password != password and not condition:
    if count<limit:
        in_user = input("Enter your username: ")
        in_password = input("Enteryour password: ")
        count += 1
        print(f"you have only {limit - count}")
    if in_user==user and in_password==password:
           print("completed")
    else:
        condition=True
        print(f"you had used {count} times ")
        print("please click the link below to take the contact with our support")



















'''
count=0
limit=3
condition = False
while in_user != user and in_password != password and not condition:
    in_user = input("Enter your username: ")
    in_password = input("Enter your password: ")
    if count < limit:
        print("Not found")
        print("please try again to write your right username and password")
        count += 1
    elif in_user ==user and in_password == password
    else:
        condition = True

print(f"You used {count} trys")
print("please click the link below to contact with our support")
'''

