# Uppercase Names

names = ["ali", "sara", "umer", "wajahat", "kamal"]


def uppercase(names):
    # upperNames = []
    # for name in names:
    #     upperNames.append(name.upper())

    # return upperNames

    return [name.upper() for name in names] # in one line


print(uppercase(names))