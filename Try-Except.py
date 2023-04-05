try:
    name = str(input("Enter your name: "))
    x = float(input("Enter a number: "))
    y = float(input("Enter a number: "))
    total = float(x) + float(y)

except ValueError:
    print('You did not enter a number, try again.')

print(f"The sum of {x} and {y} is {total}")
