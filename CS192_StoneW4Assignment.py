name = input("Enter a name or 'q' to quit: ")
while name != "q":
    account_bal = float(input("Enter account balance: $"))
    amount = float(input("Enter amount to withdraw (-) or deposit (+): $"))
    if account_bal > amount:
        new_account_bal = account_bal + amount
        print("Your account balance is: $", round(new_account_bal, 2))
    elif account_bal < amount:
        new_account_bal = account_bal - amount
        print("Your account balance is: $", round(new_account_bal, 2))
    else:
        print("Your account balance is zero.")
    name = input("Enter a name or 'q' to quit: ")
