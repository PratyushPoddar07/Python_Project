import re

def is_valid_email(email):
    # Minimum email length and starting with an alphabet
    if len(email) < 6 or not email[0].isalpha():
        print("Email must be at least 6 characters long and start with an alphabet.")
        return False

    # Check for exactly one '@' symbol
    if email.count("@") != 1:
        print("Email must contain exactly one '@' symbol.")
        return False

    # Extract username, domain, and TLD parts
    username, domain_tld = email.split("@")
    if "." not in domain_tld:
        print("Email domain must contain a '.' symbol.")
        return False

    domain, tld = domain_tld.rsplit(".", 1)

    # Validate top-level domain (TLD)
    if len(tld) not in (2, 3):  # Typically 2 or 3 characters (.in, .com, etc.)
        print("Invalid top-level domain (TLD).")
        return False

    # Check if username has invalid characters or spaces
    if re.search(r'\s', username):
        print("Username part should not contain spaces.")
        return False

    if not username.replace(".", "").replace("_", "").isalnum():
        print("Username can only contain letters, digits, dots, and underscores.")
        return False

    # Check domain format (no invalid characters)
    if not domain.isalnum():
        print("Domain part should only contain letters and digits.")
        return False

    # Check if special characters are consecutive or at invalid positions
    if ".." in email or "__" in email or ".@" in email or "@." in email or email[0] in "._" or email[-1] in "._":
        print("Email contains consecutive special characters or starts/ends with invalid characters.")
        return False

    # Validate that there are no capital letters in the email
    if any(char.isupper() for char in email):
        print("Email should not contain uppercase letters.")
        return False

    print("Email is valid.")
    return True

# Get input from user
email = input("Enter your email: ")
is_valid_email(email)
