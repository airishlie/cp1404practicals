# Password Check with Functions
PASSWORD_LENGTH = 10

def main() :
    password = get_password()

    display_asteriks(password)


def display_asteriks(password):
    """Display asteriks equal to the length of the password"""
    print(password * "*")


def get_password():
    """Asks the user for a password and ensures that the length is not shorter than the password length"""
    password = len(input("Enter password : "))
    while password <= PASSWORD_LENGTH:
        print("Invalid Password")
        password = len(input("Enter password : "))
    return password


main()