u_input = ""
u_operator = ""
operators = ['*', '/', '-', '+']

while True:
    u_operator = ""
    print('Here are your possible inputs:\n')
    print('''"x", or "q" to exit the programme.
    "l" to load the last equation you ran.
    Or enter numbers, separated by comma (,) or space ( )
    ''')
    u_input = input('Your input: ')
    if u_input == "l":
        try:
            with open('CalcHistory.txt', 'r') as CalcHistory:
                last_eq = CalcHistory.readlines()[-1]
                print('Your last equation was: ' + last_eq)
        except IndexError:
            print('There are no equations saved yet.')
    elif u_input != "x" and u_input != "q":
        substrings = u_input.split(",")
        print(substrings)
        numbers = []
        for i in substrings:
            for num in i.split():
                numbers.append(num)
                print(numbers)
        while u_operator not in operators:
            print('Acceptable operations are addition (+), substraction (-), multiplication (*), and division (/)')
            u_operator = input('Which operator would you like to use? ')
            if u_operator not in operators:
                print('Please enter a valid operator!')
            equation = u_operator.join(numbers)
            result = eval(equation)
            print(equation, "=", result)
            with open('CalcHistory.txt', 'a') as CalcHistory:
                CalcHistory.write(equation + "=" + str(result) + "\n")
    else:
        print('Goodbye!')
        break


