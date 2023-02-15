end = int(input("Enter a number: "))

fibonacci = [0, 1]

while fibonacci[-1] + fibonacci[-2] < end:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)
