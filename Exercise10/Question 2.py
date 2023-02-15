import getpass

PIN = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    supplied_pin = getpass.getpass(prompt='Enter your PIN: ')
    if supplied_pin == PIN:
        print("You're in!")
        break
    else:
        if attempts < max_attempts:
            attempts += 1
            print("Wrong PIN!")
            if attempts == 3:
                print("Your account has been locked.")
            else:
                print(f"You have {max_attempts-attempts} attempts left.")


# PIN = "1234"
# attempts = 3
#
# while attempts > 0:
#     supplied_pin = (input("Enter your PIN: "))
#     if supplied_pin == PIN:
#         print("You're in!")
#         break
#     else:
#         attempts -= 1
#         if attempts == 0:
#             print("Your account has been blocked.")
#         else:
#             print(f"Incorrect PIN. You have {attempts} attempts left.")

