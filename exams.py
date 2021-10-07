
def gets_a_zero(total_classes, class_missed):
    if int(class_missed)/int(total_classes) >= 1/4:
        return True
    else:
        return False
def main():
    total_classes = input("how many classes have you had?")
    class_missed = input("how many classes have you missed?")