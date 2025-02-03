# Password Check with Functions
PASSWORD_LENGTH = 10

def main() :
    password = get_password()

    print_asteriks(password)


def print_asteriks(password):
    print(password * "*")


def get_password():
    password = len(input("Enter password : "))
    while password <= PASSWORD_LENGTH:
        print("Invalid Password")
        password = len(input("Enter password : "))
    return password


main()