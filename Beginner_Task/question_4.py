# Stock Alert (Out of Stock)

stock = {"apple": 5, "banana": 0, "orange": 10, "pineaple": 0}


for product, qty in stock.items():
    status = "is out of stock" if qty == 0 else "is in stock"
    print(f"{product} {status}")
