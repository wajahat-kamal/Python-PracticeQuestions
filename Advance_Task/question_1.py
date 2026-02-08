products = []
num = int(input("How many Products: "))

for i in range(num):
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    qty = int(input("Enter product quantity: "))
    products.append({"name": name, "price": price, "qty": qty})


total = 0
for product in products:
    subTotal = product["price"] * product["qty"]
    total += subTotal
    print(f"{product["name"]} X {product["qty"]} = {subTotal}")

tax = total - (total * 0.10)
total += tax

if total >= 1000:
    discount = total - (total * 0.5)
    total += discount


print(total)
