# ATM Withdrawal System

balance = int(input("Enter your bank balance: "))
amount = int(input("Enter your amount: "))


def atm_withdrawal_system(balance, amount):
    if amount <= 0:
        return "Invalid Amount"

    transaction_fee = round(amount * 0.02, 2)

    if balance < (amount + transaction_fee):
        return "Insufficient Balance"

    total_deduction = amount + transaction_fee
    new_balance = round(balance - total_deduction, 2)

    return {"Updated Balance": {new_balance}, "Transaction Fee 2%": {transaction_fee}}


print(atm_withdrawal_system(balance, amount))
