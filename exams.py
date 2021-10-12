
def gets_a_zero(total_classes, class_missed):
    if int(class_missed)/int(total_classes) >= 1/4:
        return True
    else:
        return False
def main():
    total_classes = input("how many classes have you had?")
    class_missed = input("how many classes have you missed?")

    if gets_a_zero(total_classes, class_missed):
        print("because you have missed", class_missed, "class(es) you will be getting a 0 on the exam")
    else:
        print("because you have attended over 75% of your classes you can take the exam.")
if __name__ == '__main__':
    main()