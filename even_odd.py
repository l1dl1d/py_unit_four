
def even_or_odd(x):
    if x%2 == 0:
        return(str(x)+" is an even number")
    if x%2 == 1:
        return(str(x)+" is an odd number")


    """
    Create a function that will tell if a number is even or odd. Use two if statements to do this.
    :param number: could be any positive or negative integer
    :return: either "x is an even number" or "x is an odd number"
    """
    pass


def main():
    # First, make sure to delete the word "pass" then get input from the user.
    # They should type in a number, make sure to convert it to an int
    # Next, call the even_or_odd function, and make sure to pass the user's number as a parameter.
    x = input("enter number")
    # int(even_or_odd(x))


if __name__ == '__main__':
    main()