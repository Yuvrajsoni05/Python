class Student():
    def __init__(self,name):
        self.name = name
s1=Student("James")
print(s1.name)
del s1.name
print(s1)

#private
class Bank_account:
    def __init__(self,account_no,account_password):

        self.account_no =account_no
        self.__account_password = account_password
    def reset_password(self):
        return self.__account_password
        # return "We have reset your password"

ac = Bank_account(account_no="123",account_password="94995612")
print(ac.reset_password())
