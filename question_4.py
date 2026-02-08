# Stock Alert (Out of Stock)

stock = {"apple": 5, "banana": 0, "orange": 10, "pineaple": 0}


def stock_qty(stock):
    for product, qty in stock.items():
        if qty == 0:
            return f"{product} is out of stock"
        else:
            f"{product} is in stock"
print(stock_qty(stock))