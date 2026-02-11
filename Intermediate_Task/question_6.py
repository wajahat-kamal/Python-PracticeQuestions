# ATM Withdrawal System

balance = int(input("Enter your bank balance: "))
amount = int(input("Enter your amount: "))


def atm_withdrawal_system(balance, amount):
    if amount <= 0:
        return "Invalid Amount"
    if balance < amount:
        return "Insufficient Balance"


    transaction_fee = round(amount * 0.02, 2) 
    total_deduction = amount + transaction_fee
    new_balance = balance - total_deduction

    return f"Updated Balance: {new_balance} \nTransaction Fee 2%: {transaction_fee}"


print(atm_withdrawal_system(balance, amount))
