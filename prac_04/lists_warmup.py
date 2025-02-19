numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])      # 3
print(numbers[-1])     # 2
print(numbers[3])      # 1
print(numbers[:-1])    # [3, 1, 4, 1, 5, 9]
print(numbers[3:4])    # [1]
print(5 in numbers)    # True
print(7 in numbers)    # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


numbers[0] = "ten"  # 1. Change the first element to ten
numbers[-1] = 1     # 2. Change the last element to 1

# 3. print all element except the first two numbers
print(numbers[2:])

# 4. Check if 9 is in the list
print(9 in numbers)