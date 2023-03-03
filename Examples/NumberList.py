import random

# Create a list of numbers from 1 to 100
numbers = list(range(1, 101))

# Remove a random amount of numbers from the list, leaving at least one number remaining
for i in range(random.randint(1, len(numbers)-1)):
    numbers.remove(random.choice(numbers))

# Find the missing numbers in the list
missing_numbers = []
for i in range(1, 101):
    if i not in numbers:
        missing_numbers.append(i)

# Print the results
print("Your list:", numbers)
print("The list is missing", (100-len(numbers)), "numbers.")
print("Missing numbers:", missing_numbers)

# Duplicate a random number in the list
numbers.append(random.choice(numbers))

# Only sorted the list to not have the duplicate number at the end, search code does not require a sorted list
# Calling .sort() is obsolete and would usually be avoided to reduce possible impact on performance
numbers.sort()
print("Your list including a duplicated number:", numbers)

duplicated_number = None

# for loop runs through list and checks if the number at index i is in the list of numbers before and after index
for i in range(len(numbers)):
    if numbers[i] in numbers[:i] + numbers[i+1:]:
        duplicated_number = numbers[i]
        break

# Print the duplicated number
print("The duplicated number is", duplicated_number)
