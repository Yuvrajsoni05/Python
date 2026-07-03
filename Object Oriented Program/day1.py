class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc
    def debit_card(self,amount):
        self.bal =  self.bal - amount
        print("Your balance is",self.bal)
        print("Total amount is",self.get_balance())
    def credit_card(self,amount):
        self.bal = self.bal + amount
        print("Your balance is",self.bal)
        print("Total amount is",self.get_balance())

    def get_balance(self):
        return self.bal



account1 = Account(1000000,100)
print(account1.bal)
print(account1.acc)

account1.debit_card(100)
account1.debit_card(10000)






