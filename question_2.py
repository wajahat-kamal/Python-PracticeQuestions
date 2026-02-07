# Price After Discount

price = int(input("Enter the price: "))
discount = int(input("Enter the discount: "))

def discount_func(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

print(discount_func(price, discount))