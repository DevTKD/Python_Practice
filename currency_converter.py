"""
💵 Currency Converter (Version 1)
Convert an amount from one currency to another using a predefined exchange rate.
"""
# Dictionary to store exchange rates
exchange_rates = {
    "EUR": 0.96,
    "USD": 1.0,
    "GBP": 0.82,
    "JPY": 110.0,
    "CAD": 1.44
}

currency_amount = float(input("Enter currency amount: "))
print("Currency Options: EUR, USD, GBP, JPY or CAD")
from_currency = input("Enter original currency: ")
target_currency = input("Enter wanted currency: ")

# Check if the target currency is in the dictionary
if target_currency in exchange_rates:
    calculated_exchange_currency = currency_amount * exchange_rates[target_currency]
    print(f"Your currency exchange is {calculated_exchange_currency} {target_currency}")
else:
    print("Enter a valid currency.")