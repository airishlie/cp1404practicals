"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
result= ""
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is : result {result}")