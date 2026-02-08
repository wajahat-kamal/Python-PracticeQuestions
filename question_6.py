# Total Bill (Sum of Items)

prices = [250, 100, 340, 120]

def sum(prices):
    total = 0
    for price in prices:
        total += price

    return f"Total bill is {total}"

print(sum(prices))
