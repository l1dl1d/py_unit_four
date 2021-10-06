def salary_calculation(salary, yearly_amount):
    if int(yearly_amount) > 5:
        return salary*0.05+salary
    else:
        return salary
def main():
    salary = float(input("what is your salary?"))
    year_amount = input("how long have you worked here?")
    salary_calculation(salary, year_amount)
main()