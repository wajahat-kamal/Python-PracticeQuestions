# Uppercase Names

names = ["ali", "sara", "umer", "wajahat", "kamal"]


def uppercase(names):
    upperNames = []
    for name in names:
        upperNames.append(name.upper())

    return upperNames


print(uppercase(names))