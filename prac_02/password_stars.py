# Password Check with Functions
PASSWORD_LENGTH = 10

def main() :
    """Display asteriks equal to the length of the password"""
    password = validate_password()
    print(password * "*")


def validate_password():
    """Get a valid password"""
    password = len(input("Enter password : "))
    while password < PASSWORD_LENGTH:
        print("Invalid Password")
        password = len(input("Enter password : "))
    return password


main()