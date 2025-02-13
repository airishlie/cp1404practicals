# 1.  Ask for the user's name and write it to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as out_file:
    out_file.write(name)

# 2. Read from 'name.txt' and print the name in the format "Hi Bob!"
with open('name.txt', 'r') as in_file:
    name_from_file = in_file.read().strip()
    print(f"Hi {name_from_file}!")

# 3. Add the first two numbers in 'numbers.txt' and print the result
with open('numbers.txt', 'r') as in_file:
    number_1 = int(in_file.readline().strip())
    number_2 = int(in_file.readline().strip())
    print(number_1 + number_2)

# 4. Calculate the total of all numbers in 'numbers.txt'
with open('numbers.txt', 'r') as in_file:
    total = sum(int(line.strip()) for line in in_file)
    print(total)