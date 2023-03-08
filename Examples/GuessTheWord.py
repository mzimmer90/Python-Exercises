def check_word(check, word):
    if word == check:
        print("Correct")
    else:
        print("Incorrect")


set_word = "test"
u_word = input("Enter your word:").lower()
check_word(set_word.lower(), u_word)
