# Initialise variables
u_input = ""
u_operator = ""
operators = ['*', '/', '-', '+']

# Begin an infinite loop
while True:

    # Reset the operator variable
    u_operator = ""

    # Print instructions for the user
    print('Here are your possible inputs:\n')
    print('''"x", or "q" to exit the programme.
"l" to load the last equation you ran.
Or enter numbers, separated by comma (,) or space ( )
    ''')

    # Get user input
    u_input = input('Your input: ')

    # If the user entered "l", load the last equation from CalcHistory.txt
    if u_input == "l":
        try:
            with open('CalcHistory.txt', 'r') as CalcHistory:
                last_eq = CalcHistory.readlines()[-1]
                print('Your last equation was: ' + last_eq)
        except FileNotFoundError:
            print('The history file does not exist yet. Please complete at least one equation.')
        except IndexError:
            print('There are no equations saved yet.')

    # If the user didn't enter "l", check if they entered "x" or "q"
    elif u_input not in ["x", "q"]:

        # Split the user input into substrings
        substrings = u_input.split(",")
        print(substrings)  # debugging use

        # Initialize a list to store the numbers in the user input
        numbers = []

        # Loop through the substrings and split them into individual numbers
        for i in substrings:
            for num in i.split():
                # Validate the number before appending to the list
                try:
                    num = int(num)
                    numbers.append(str(num))
                except ValueError:
                    print('Please enter a valid input!')
                    break
                print(numbers)  # debugging use
            else:
                continue
            break

        # Loop until the user enters a valid operator
        while u_operator not in operators:

            # Print instructions for the user
            print('Acceptable operations are addition (+), subtraction (-), multiplication (*), and division (/)')

            # Get user input for the operator
            u_operator = input('Which operator would you like to use? ')

            # If the user entered an invalid operator, prompt them to try again
            if u_operator not in operators:
                print('Please enter a valid operator!')

        # Join the numbers into an equation using the chosen operator
        equation = u_operator.join(numbers)

        # Evaluate the equation and print the result
        result = int(numbers[0])
        for i in range(1, len(numbers)):
            if u_operator == '+':
                result += int(numbers[i])
            elif u_operator == '-':
                result -= int(numbers[i])
            elif u_operator == '*':
                result *= int(numbers[i])
            elif u_operator == '/':
                result /= int(numbers[i])

        print(equation, "=", result)

        # Write the equation and result to CalcHistory.txt
        with open('CalcHistory.txt', 'a') as CalcHistory:
            CalcHistory.write(equation + "=" + str(result) + "\n")

    # If the user entered "x" or "q", exit the loop
    else:
        print('Goodbye!')
        break
