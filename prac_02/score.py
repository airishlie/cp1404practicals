import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main ():
    score = float(input("Enter score: "))
    result = evaluate_score (score)
    print(result)

    random_score = random.randint(MINIMUM_SCORE,MAXIMUM_SCORE)
    print(f"Random score: {random_score}")
    print(evaluate_score(random_score))


def evaluate_score (score) :
    """Checks if the score is valid and display the result of the score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif  score >= 50:
        return "Passable"
    else :
        return "Bad"
main()