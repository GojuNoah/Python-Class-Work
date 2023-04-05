name = input("What's your name? ")
gross_income = float(input("What's your gross income? "))
state_tax_rate = float(input("What's your state tax rate? "))

Federal_tax = gross_income * float(.0945)
FICA_tax = gross_income * float(.0765)
State_tax = gross_income * (state_tax_rate*float(0.01))

estimate = round(Federal_tax + FICA_tax + state_tax_rate, 2)

print(name)
print(gross_income)
print(estimate)
