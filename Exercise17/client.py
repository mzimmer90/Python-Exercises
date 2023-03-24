from account import Account, InsufficientFundsException

account1 = Account(100)
print(account1)
account1.withdraw(40)
#account1.withdraw(50)
print(account1)
try:
    account1.withdraw(51)
    print(account1)
except InsufficientFundsException as err:
    print("Oops:", err)
