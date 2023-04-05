name = input("What is your name? ")
amount1 = float(input("Enter an  amount: "))
amount2 = float(input("Enter an  amount: "))
amount3 = float(input("Enter an  amount: "))
amount4 = float(input("Enter an  amount: "))
amount5 = float(input("Enter an  amount: "))

bal = amount1 + amount2 + amount3 + amount4 + amount5

if bal > 0:
    print("Your account balance is: $" + "%.1f"% bal)
elif bal == 0:
    print("Your account balance is zero")
else:
    print("Your account is overdrawn. The overdrawn amount is: $" + "%.1f"% bal)
