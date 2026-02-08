# Find User

users = ["ali", "sara", "umer", "wajahat", "kamal"]


def check_user(users):
    username = input("Enter your name: ")
    return "User Exists" if username in users else "User not found"


print(check_user(users))
