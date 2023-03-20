# Define the max number of * in the pattern
max_ast = int(input("Enter the max number of *: "))

# Loop through each row of the pattern
for i in range(max_ast * 2 - 1):

    # Determine the number of asterisks to print in this row
    if i < max_ast:
        num_ast = i + 1
    else:
        num_ast = max_ast * 2 - i - 1

    # Print the asterisks for this row
    for j in range(num_ast):
        print("* ", end="")

    # Move to the next line
    print()
