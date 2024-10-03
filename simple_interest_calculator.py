"""
    Calculate the simple interest.

    :param principal: The initial amount of money (P).
    :param rate: The annual interest rate (r) as a decimal.
    :param years: The time the money is invested for in years (t).
"""
principal = float(input("Enter the initial amount of money (P): "))
rate = float(input("Enter the interest rate (r): "))
time = float(input("Enter the time the money is invested for in years (t): "))

simple_interest = principal * rate * time / 100

print(f"The simple interest of the inputted parameter is {simple_interest}")
