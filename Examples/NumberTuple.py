from math import prod
import random

# Generate random length tuple filled with random numbers
MyTup = tuple(random.randint(1, 100) for _ in range(random.randint(1, 25)))
print("Your tuple has", len(MyTup), "elements, which are:")
print(MyTup)

# Calculate the difference between biggest and smallest number in tuple
print("The difference of the largest and smallest item is", max(MyTup) - min(MyTup))

# Calculate the product (multiplication) of all the values in the tuple
print("The product of all items is", prod(MyTup))

