while True:
    user_input = input("Enter the number you want to run Primes up to: ")
    try:
        num_stop = int(user_input)
        break
    except ValueError:
        print("Please enter a valid whole number.")

primes = []
primes_str = []
for num in range(2, num_stop):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        primes.append(num)

prime_str = ", ".join(str(p) for p in primes)
print("Here are your primes: " + prime_str)

# i = 0
# while i < len(primes):
#     if primes[i] % 2 != 0:
#         primes_str.append(str(primes[i]))
#     i += 1
#
# print("Here are your primes: " + ", ".join(primes_str))



