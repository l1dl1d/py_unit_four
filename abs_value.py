def abs_value(x):
    if float(x) < 0:
        return x*-1
    else:
        return x
def main():
    x = float(input("please enter a number:"))
    print(abs_value(x))
main()