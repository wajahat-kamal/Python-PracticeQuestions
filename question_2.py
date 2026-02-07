# Price After Discount

price = int(input("Enter the price: "))
discount = int(input("Enter the discount: "))

def discount_func(price, discount):
    discount = price - (price * discount / 100)
    return discount

print(discount_func(price, discount))