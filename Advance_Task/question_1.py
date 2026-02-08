# Mini Invoice Generator

products = []

def invoice_generator(products):
    num = int(input("How many Products? "))

    for i in range(num):
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        qty = int(input("Enter product quantity: "))
        products.append({"name": name, "price": price, "qty": qty})

    total = 0
    for product in products:
        subTotal = product["price"] * product["qty"]
        total += subTotal
        print(f"{product['name']} X {product['qty']} = {subTotal}")

    tax = round(total * 0.10, 2)
    discount = round(total * 0.05 if total >= 5000 else 0, 2)
    final_amount = round(total + tax - discount, 2)

    print(f"{'Total before tax:':<20} {total}")
    print(f"{'Tax (10%):':<20} {tax}")
    print(f"{'Discount (5%):':<20} {discount}")
    print(f"{'Final amount:':<20} {final_amount}")


invoice_generator(products)
