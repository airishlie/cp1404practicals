import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

def main ():
    """display grade"""
    score = validate_score()
    grade = get_grade(score)
    print(grade)
    random_number = random.uniform(MINIMUM_SCORE,MAXIMUM_SCORE)
    #print random number
    random_grade = get_grade(random_number)
    print (random_grade)

def get_grade(score):
    """Determine grade base on the score"""
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else :
        message = "Bad"
    return message

def validate_score () :
    """Checks if the score is valid"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print ("Invalid score")
        score = float(input("Enter score : "))
    return score

main()