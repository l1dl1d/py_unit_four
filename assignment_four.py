import random
def get_card():
    random_num = random.randint(1, 10)
    return random_num
def get_winner(user, dealer):
    user_total = input("you drew a", random.randint(1, 10), "and a", random.randint(1, 10), "your total is" )
    dealer_total = input("the dealer has a", random.randint(1, 10), "and a", random.randint(1, 10))

    if user_total >= 21:
        print("You went over 21. You lose")
    elif user_total > dealer_total:
        print(dealer_total, "You Won!")
    elif user_total < dealer_total:
        print(user_total, "The dealer won")
    else:
        print("it was a tie")
def main(user_total, get_card)

