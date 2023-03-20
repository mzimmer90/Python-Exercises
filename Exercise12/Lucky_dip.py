from lotto import Lotto
from lotto_packages.lotto_functions import check_match_count
import random

Lotto_Numbers = random.sample(range(1, 51), 6)

tickets = []
ticket_amount = int(input("How many tickets would you like?"))

for i in range(ticket_amount):
    tickets.append(Lotto())

print("\nChecking Lotto Numbers...")
print(f"Today's numbers are: {Lotto_Numbers} \n")

for i in tickets:
    check_match_count(i, Lotto_Numbers)
