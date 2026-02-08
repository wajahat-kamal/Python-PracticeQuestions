# Stock Alert (Out of Stock)

stock = {
    "apple": 5,
    "banana": 0,
    "orange": 10
}


def stock_alert(stock):
    if stock > 0:
        print("In Stock")
    else:
        print("Out of Stock")

stock_alert(stock["apple"])