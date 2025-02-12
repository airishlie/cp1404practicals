# Stock-price simulator for a volatile stock

import random

STARTING_PRICE = 10.00
MINIMUM_PRICE = 1.00
MAXIMUM_PRICE = 100.00
MAXIMUM_INCREASE = 0.175  # 17.5%
MAXIMUM_DECREASE = 0.05  # 5%
FILENAME = "stock_price_simulation.txt"

price = STARTING_PRICE
number_of_days = 0

out_file = open(FILENAME, 'w')

print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate stock price changes
while MINIMUM_PRICE >=  price or price <= MAXIMUM_PRICE:
    number_of_days += 1
    # 50% chance for increase or decrease
    if random.randint(0, 1) == 0:
        # Decrease price by up to 5%
        decrease_amount = random.uniform(0, MAXIMUM_DECREASE)
        price -= price * decrease_amount
    else:
        # Increase price by up to 17.5%
        increase_amount = random.uniform(0, MAXIMUM_INCREASE)
        price += price * increase_amount

    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()

print(f"Simulation ended after {number_of_days} days.")