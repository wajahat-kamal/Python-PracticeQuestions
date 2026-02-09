# Transaction History Analyzer

transactions = [2000, -500, -300, 1500, -1000]


def transaction_analyzer(transactions):
    credit = 0
    debit = 0
    total_balance = sum(transactions)
    for transaction in transactions:
        if transaction > 0:
            credit += transaction
        else:
            debit += abs(transaction)

    warning = ""
    if total_balance < 0:
        warning = "Warning: Your balance is negative!"

    return f"Total Credit: {credit} \nTotal Debit: {debit} \nTotal Balance: {total_balance} \n {warning}"


print(transaction_analyzer(transactions))
