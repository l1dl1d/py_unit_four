# Khalid
# date: 10/22/21
# The purpose of this program is to generate a black jack game to play and to interact with.
import random
def get_card():
    """
    this function draws a random card between 1 and 10
    :return: returns the random number
    """
    random_num = random.randint(1, 10)
    return random_num

def get_winner(user_total, dealer_total):
    """
    this function gives the dealers total and users total then declares who won and how.
    :param user_total: this is the users total at the moment
    :param dealer_total: this tells the dealers total
    :return:
    """
    if user_total > 21:
        return "You went over 21. You lose"
    elif user_total > dealer_total:
        return "the dealers total is " + str(dealer_total) + " You Won!"
    elif user_total < dealer_total:
        return "the dealers total is " + str(dealer_total) + " the dealer won"
    else:
        return "it was a tie"

def main():
    """
    this function is where all the text happens. it asks if you want another card and it calls all of
    the other functions to put everything together
    :return:
    """
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