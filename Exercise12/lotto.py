import random


class Lotto:
    def __init__(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.numbers = []
        self.roll_numbers()

    def roll_numbers(self):
        self.numbers = random.sample(range(1, 51), 6)

    def print_numbers(self):
        print("Lotto Numbers: ", end="")
        for num in self.numbers:
            print(num, end=" ")
        print()
