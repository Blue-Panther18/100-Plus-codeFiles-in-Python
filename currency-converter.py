'''
converts a particular amount from one currency to another specified by the user.
'''

def curr_converter(amount, from_currency, to_currency):
    # Dictionary with some example exchange rates relative to USD
    exchange_rates = {
        "USD": 1,        # US Dollar
        "EUR": 0.85,     # Euro
        "GBP": 0.75,     # British Pound
        "INR": 74.57,    # Indian Rupee
        "JPY": 110.0,    # Japanese Yen
        "CAD": 1.25,     # Canadian Dollar
    }

    # Ensuring the currencies are in the exchange rate dictionary.
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency codes."
    
    # converting the currency to usd first before the desired currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    return round(converted_amount, 2)

amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency code to be converted form: ").upper()
to_currency = input("Enter the currency code to be converted to: ").upper()

converted_amount = curr_converter(amount, from_currency, to_currency)

print(f"{amount} {from_currency} is {converted_amount} {to_currency}")
