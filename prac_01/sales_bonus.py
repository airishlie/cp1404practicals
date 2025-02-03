"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MINIMUM_SALES = 0
DISCOUNT_THRESHOLD = 1000
MINIMUM_DISCOUNT = 0.1
MAXIMUM_DISCOUNT = 0.15

sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALES:
    if sales < DISCOUNT_THRESHOLD:
        bonus = MINIMUM_DISCOUNT
    else :
        bonus = MAXIMUM_DISCOUNT
    bonus_received = bonus * sales
    print (f"You get $ {bonus_received:.2f} as a bonus")
    sales = float(input("Enter sales: $"))