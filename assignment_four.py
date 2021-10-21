import random
def get_card():
    random_num = random.randint(1, 10)
    return random_num

def get_winner(user_total, dealer_total):
    if user_total > 21:
        return "You went over 21. You lose"
    elif user_total > dealer_total:
        return "the dealers total is " + str(dealer_total) + " You Won!"
    elif user_total < dealer_total:
        return "the dealers total is " + str(dealer_total) + " the dealer won"
    else:
        return "it was a tie"

def main():
    card1 = get_card()
    card2 = get_card()
    card3 = get_card()
    card4 = get_card()
    user_total = card1 + card2
    dealer_total = card3 + card4

    print("you drew a ", card1,"and a", card2, "your total is", user_total)
    want_card = input("would you like another card?")
    if want_card == "y":
        """
        if the user wants another card this if statement allows them to press y for another one. a new randomly generated 
        card will be added to the total of the user_total.
        """
        card5 = get_card()
        user_total = user_total + card5
        print("your total is now", user_total)
    print("the dealer has a ", card3, "and a", card4 )
    print(get_winner(user_total, dealer_total))
    return

if __name__ == '__main__':
    main()