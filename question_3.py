# Empty or Not (Check List)

list1 = []
list2 = ["apple", "banana", "pineapple"]

def check_list(list):
    if len(list) == 0:
        return "List is empty"
    else:
        return "List has items"


print(check_list(list1))
print(check_list(list2))
