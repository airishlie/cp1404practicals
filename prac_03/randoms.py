import random

print(random.randint(5, 20))# line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# = line 1 will generate a random integer between 5 and 20 (inclusive)
# What was the smallest number you could have seen, what was the largest?
# = Smallest number : 5
# = Largest number : 20

# What did you see on line 2?
# = Line 2 will generate a random number from 3 to 9 (exclusive of 10) using a step of 2
# What was the smallest number you could have seen, what was the largest?
# = Smallest number = 3
# = Largest number = 9
# Could line 2 have produced a 4?
# No, line 2 could not produced a 4, because the step is 2.

# What did you see on line 3?
# = Line 3 will generate a random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# = Smallest Number = 2.5
# = Largest Number = 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)

print(random_number)