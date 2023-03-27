class Account:
    def __init__(self, amount):
        self._balance = amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            raise InsufficientFundsException()
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"Your account balance: £{self._balance}"


class InsufficientFundsException(Exception):
    def __str__(self):
        return "Not enough funds in your account"
