# def pal_check(x):
#     reverse_x = x[::-1]
#     if x == reverse_x:  # "".join(reversed(x)):
#         return True
#
#
# end_range = 100
# for i in range(10, 500):
#     if pal_check(str(i)):
#         print(i, "Is a palindromic number")


def pal_check(x):
    palindromes = []
    for i in range(int(x)+1):
        reverse_i = str(i)[::-1]
        if str(i) == reverse_i:  # "".join(reversed(i)):
            palindromes.append(i)
            # print(i, "Is a palindromic number")
    print("Palindromic numbers in your range are:", ', '.join(map(str, palindromes)))


pal_check("494")
