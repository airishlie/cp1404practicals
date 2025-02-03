# Display all the odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars on one line
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end='')
print()

# d. Print n lines of increasing stars
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()

