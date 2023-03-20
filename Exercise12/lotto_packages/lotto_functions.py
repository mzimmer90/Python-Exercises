def check_match_count(ticket, lotto_numbers):
    matched_numbers = set(ticket.numbers).intersection(set(lotto_numbers))
    match_count = len(matched_numbers)
    if match_count == 0:
        print(f"Sorry {ticket.first_name} {ticket.last_name}, you had matched no numbers. Better luck next time.")
    elif match_count == 6:
        print(f"Congratulations {ticket.first_name} {ticket.last_name}, you won the jackpot!")
    else:
        print(f"{ticket.first_name} {ticket.last_name} matched {match_count} numbers: {matched_numbers}.")
    print()
