# Email Validator

email = input("Enter your email: ")

def email_validator(email):
    check = "Valid Email" if "@" in email and "." in email else "Invalid Email"
    return check

print(email_validator(email))