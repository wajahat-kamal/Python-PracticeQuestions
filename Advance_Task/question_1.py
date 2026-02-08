products = []
num = int(input("How many Products: "))

for i in range(num):
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    qty = int(input("Enter product quantity: "))
    products.append({"name": name, "price": price, "qty": qty})


total = 0
subTotal = price * qty
tax = subTotal + (subTotal * 0.10)
total += tax

if total >= 1000:
    discount = total - (total * 0.5)
    total += discount


print(total)
