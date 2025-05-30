"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month} : "))
        incomes.append(income)

    calculate_income(incomes, number_of_months)


def calculate_income(incomes, number_of_months):
    """Calculate and display income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate (incomes, start=1):
        total += income
        display_report(month,income,total)
    return total

def display_report (month,income,total) :
    """Print details of income for each month and the total"""
    print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()