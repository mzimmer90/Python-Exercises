from random import randint


# Define a function that converts a single letter hand input to its full word form using a dictionary
def hand_convert(h_convert):
    return {
        "R": "rock",
        "P": "paper",
        "S": "scissors"
    }[h_convert]


# Define a function that plays a round of Rock-Paper-Scissors and updates scores
def rps_game(u_choice, c_choice, u_temp_score, c_temp_score):
    # Print the choices made by the user and computer (mainly debugging)
    print("You picked", u_hand)
    print("The computer picked", c_hand)
    # Nested if-block to determine the winner and increase the scores accordingly
    if u_choice == c_choice:
        print("Tie!")
    elif u_choice == "rock":
        if c_choice == "paper":
            c_temp_score += 1
            print("You lose! Paper covers rock.")
        else:
            u_temp_score += 1
            print("You win! Rock smashes scissors.")
    elif u_choice == "paper":
        if c_choice == "scissors":
            c_temp_score += 1
            print("You lose! Scissors cut paper.")
        else:
            u_temp_score += 1
            print("You win! Paper covers rock.")
    elif u_choice == "scissors":
        if c_choice == "rock":
            c_temp_score += 1
            print("You lose! Rock smashes scissors.")
        else:
            u_temp_score += 1
            print("You win! Scissors cut paper.")
    # Return the updated scores
    return u_temp_score, c_temp_score


# Set the initial scores for the user and computer to 0
c_score = 0
u_score = 0
# Create a list of the three possible choices in the game
hands = ['rock', 'paper', 'scissors']
# Initialise a variable to hold the user's input
u_hand = ""
# Loop until the user inputs a valid letter
while u_hand not in ['R', 'P', 'S', 'X', 'Q']:
    u_hand = input("Please enter your hand, 'R', 'P', or 'S'. 'X' or 'Q' to exit: ").upper()
    if u_hand in ['R', 'P', 'S']:
        # Generate a random hand for the computer picked from hand list
        c_hand = hands[randint(0, 2)]
        # Convert the user's choice to its full word form
        u_hand = hand_convert(u_hand)
        # Play a round of Rock-Paper-Scissors and update scores
        u_score, c_score = rps_game(u_hand, c_hand, u_score, c_score)
        # Print the updated scores
        print(f"You: {u_score} wins | Computer: {c_score} wins")
    # If the user inputs "X" or "Q" to exit game and print final score.
    elif u_hand in ['X', 'Q']:
        print(f"Final score\nYou: {u_score} | Computer: {c_score}")
    # If input doesn't match any of the checked criteria, prints message and returns to input
    else:
        print("Please enter a valid hand, or exit the game.")
