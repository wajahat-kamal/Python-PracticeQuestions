# Find User

users = ["ali", "sara", "umer", "wajahat", "kamal"]

def check_user(users):
    user = input("Enter your name: ")

    if user in users:
        return "User Exists"
    else:
        return "User not found"

print(check_user(users))