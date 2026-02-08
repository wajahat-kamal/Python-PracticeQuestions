# Stock Alert (Out of Stock)

stock = {"apple": 5, "banana": 0, "orange": 10, "pineaple": 0}


for product, qty in stock.items():
    if qty == 0:
        print(f"{product} is out of stock")
    else:
        print(f"{product} is in stock")
