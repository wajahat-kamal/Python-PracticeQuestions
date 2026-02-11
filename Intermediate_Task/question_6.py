# ATM Withdrawal System

balance = int(input("Enter your bank balance: "))
amount = int(input("Enter your amount: "))


def atm_withdrawal_system(balance, amount):
    if amount <= 0:
        return "Invalid Amount"
    if balance < amount:
        return "Insufficient Balance"



print(atm_withdrawal_system(balance, amount))
