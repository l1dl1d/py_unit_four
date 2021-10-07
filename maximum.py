def max(x, y):
    if int(x) > int(y):
        return int(x)
    else:
        return int(y)
def main():
    x = int(input("please enter a parameter."))
    y = int(input("please enter a parameter."))
    print(max(x, y))
if __name__ == '__main__':
    main()