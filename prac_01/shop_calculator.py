DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9
MINIMUM_ITEMS = 0

total_price = 0
number_of_items = int(input("Number of items : "))

while number_of_items < MINIMUM_ITEMS :
    print ("Invalid number of items!")
    number_of_items = int(input("Number of items : "))

for i in range (number_of_items) :
    item_price = float(input("Price of item : "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD :
    total_price *= DISCOUNT_RATE #Price after discount

print(f"Total price of {number_of_items} items is $ {total_price:.2f}")