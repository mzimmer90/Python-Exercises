from random import randint


def hand_convert(h_convert):
    if h_convert == "R":
        return "rock"
    if h_convert == "P":
        return "paper"
    if h_convert == "S":
        return "scissors"


def rps_game(u_choice, c_choice):
    global c_score
    global u_score
    if u_choice == c_choice:
        print("Tie!")
    elif u_choice == "rock":
        if c_choice == "paper":
            c_score += 1
            print("You lose! Paper covers rock.")
        else:
            u_score += 1
            print("You win! Rock smashes scissors.")
    elif u_choice == "paper":
        if c_choice == "scissors":
            c_score += 1
            print("You lose! Scissors cut paper.")
        else:
            u_score += 1
            print("You win! Paper covers rock.")
    elif u_choice == "scissors":
        if c_choice == "rock":
            c_score += 1
            print("You lose! Rock smashes scissors.")
        else:
            u_score += 1
            print("You win! Scissors cut paper.")


c_score = 0
u_score = 0
hands = ['rock', 'paper', 'scissors']
u_hand = ""
while u_hand not in ['R', 'P', 'S', 'X', 'Q']:
    u_hand = input("Please enter your hand, 'R', 'P', or 'S'. 'X' or 'Q' to exit: ").upper()
    if u_hand in ['R', 'P', 'S']:
        c_hand = hands[randint(0, 2)]
        u_hand = hand_convert(u_hand)
        print("You picked", u_hand)
        print("The computer picked", c_hand)
        rps_game(u_hand, c_hand)
        print(f"You: {u_score} wins | Computer: {c_score} wins")
    elif u_hand in ['X', 'Q']:
        print(f"Final score\nYou: {u_score} | Computer: {c_score}")
        break
    else:
        print("Please enter a valid hand, or exit the game.")
