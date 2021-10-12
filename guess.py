import random
def main():
    random_num = random.randint(1, 10)
    x = input("please guess my number:")

    if int(x) == random_num:
        print("You got it right")
    else:
        print("Oh, I am sorry, my number was", random_num,"You were", ((random_num-int(x))**2)**0.5)
if __name__ == '__main__':
    main()