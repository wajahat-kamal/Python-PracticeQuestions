# Login Check

users = {"admin": "1234", "user1": "abcd", "ali": "pass123"}

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users:
        if password == users[username]:
            return "Login Successfull!"
    else:
        return "Invalid Credentials"


print(login(users))
