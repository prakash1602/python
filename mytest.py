class Test:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount<=self.balance:
            print('Collect Cash')
            self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount
        print('Deposited')
#i change this comment
class Bank:
    def m1():
     bal=int(input('Enter your balance:'))
     acc=Test(bal)
     print('Your balance is',acc.balance)
     amt=int(input('Enter your  withdraw amount:'))
     acc.withdraw(amt)
     print('Your rest balance is',acc.balance)
     amt=int(input('Enter your deposit amount:'))
     acc.deposit(amt)
     print('Your updated balance is',acc.balance)
Bank.m1()

