# Transaction History Analyzer

transactions = [2000, -500, -300, 1500, -1000]


def transaction_analyzer(transactions):
    credit = []
    debit = []
    total_balance = sum(transactions)
    for transaction in transactions:
        if transaction > 0:
            credit.append(transaction)
        else:
            debit.append(transaction)

    return f"Total Credit: {credit} \nTotal Debit: {debit} \nTotal Balance: {total_balance}"


print(transaction_analyzer(transactions))
