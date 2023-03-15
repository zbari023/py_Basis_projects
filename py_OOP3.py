class User:
    def __init__(self,name,age):
        print(f'welcome {name}')
        self.name= name
        self.age = age
    def show_details(self):
        print(f'Name:  {self.name}')
        print(f'your age is {self.age}')
class Bank(User):
    def __init__(self):
        self.balance = 0
    def withdraw(self,amount):
        if amount > self.balance:
            print(f'you dont have enough balance : {self.balance}')
            return
        self.balance-=amount
        self.show()
    def deposite(self,amount):
        self.balance += amount
        self.show()
    def show(self):
        print(f'your current balance : {self.balance}')
c1=Bank('ahmed',23)
c1.show()