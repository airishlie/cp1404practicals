"""
Email-to-name storage program
Stores users emails and names in a dictionary with validation and formatted output

Estimated Time : 30 minutes
Actual Time : 28 February (8:30-8:50, 11:20-11:30)
"""

def main() :
    """Store emails and names in dictionary, allowing users to confirm their names"""
    email_to_name = {}

    email = input ("Email : ")
    while email :
        suggested_name = get_name_from_email(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

        if confirmation and confirmation != 'y':
            name = input("Name: ").strip()
        else :
            name = suggested_name

        email_to_name[email] = name
        email = input ("Email: ")

    print()
    for email,name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email (email) :
    """Extract a name from an email address"""
    name_part = email.split ('@')[0]
    name_parts = name_part.split('.')
    return " ".join(name_parts).title()

main()