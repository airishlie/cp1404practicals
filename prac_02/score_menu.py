MENU = """(G)et a valid score (must be 0-100)
(P)rint result 
(S)how stars
(Q)uit"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main():
    score = validate_score()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            result = evaluate_score(score)
            print(result)
        elif choice == "S":
            print ("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")

def validate_score ():
    """Checks if the user enter a valid score between 0 to 100"""
    score = int(input("Enter score : "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print ("Invalid Score!! Score must be between 0 to 100")
        score = int(input("Enter score :" ))
    return score

def evaluate_score (score) :
    """Return evaluation of the score"""
    if score >= 90:
        return "Excellent"
    elif  score >= 50:
        return "Passable"
    else :
        return "Bad"

main()