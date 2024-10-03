"""
    Calculate the compound interest.

    :param principal: The initial amount of money (P).
    :param rate: The annual interest rate (r) as a decimal.
    :param times_compounded: The number of times interest is compounded per year (n).
    :param years: The time the money is invested for in years (t).
"""

principal = float(input("Enter the initial amount of money (P): "))
rate = float(input("Enter the interest rate (r): "))
time = float(input("Enter the time the money is invested for in years (t): "))
n = int(input("Enter the number of times interest is compounded per year (n): "))

amount = principal * (1 + rate / n) ** (n * time)

print(f"The compound interest of the inputted parameter is {amount:.2f}.")