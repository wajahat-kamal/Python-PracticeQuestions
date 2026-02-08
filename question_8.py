# Password Length Check

password = input("Enter your password: ")


def check_password(password):
    # if len(password) < 8:
    #     return "Password is too short"
    # else:
    #     return "Strong Password"

    return "Password is too short" if len(password) < 8 else "Strong Password" # in one line


print(check_password(password))
