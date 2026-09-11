'''
E-Commerce Currency Converter
Scenario
An online store represents transaction totals as structured objects containing currency labels. To prevent logic errors, 
the system must not add different currencies directly and should print descriptive labels.

Problem Description
Create a class named PriceAmount with the following requirements:

Constructor (__init__): Accepts value (float) and currency (string). Standardize the currency string value by 
converting it to uppercase.
Dunder Methods for String Representation:
__str__: Returns a string formatted as "<currency> <value>" with the value rounded to 2 decimal places (e.g., "USD 19.99").
__repr__: Returns a detailed programmer representation: "PriceAmount(value=<value>, currency='<currency>')" 
(value rounded to 2 decimal places).
Operator Overloading:
__add__(self, other):
Check if other is an instance of PriceAmount and has the same currency value.
If the currency values do not match, raise a ValueError with the message: "Cannot add price amounts with different currencies: 
'<currency1>' and '<currency2>'."
If valid, return a new PriceAmount instance with the summed value and the same currency.
__eq__(self, other):
Returns True if other is an instance of PriceAmount, has the same currency, and the values are identical. Otherwise, 
returns False.
Example Walkthrough
p1 = PriceAmount(19.99, "usd")
p2 = PriceAmount(10.01, "USD")
p3 = PriceAmount(15.00, "EUR")

print(str(p1))      # Output: USD 19.99
print(repr(p1))     # Output: PriceAmount(value=19.99, currency='USD')

total = p1 + p2
print(str(total))   # Output: USD 30.00

print(p1 == PriceAmount(19.99, "USD")) # Output: True

try:
    bad_addition = p1 + p3
except ValueError as e:
    print(e)  # Output: Cannot add price amounts with different currencies: 'USD' and 'EUR'.
'''


class PriceAmount:

    def __init__(self, value, currency):
        self.value = float(value)
        self.currency = currency.upper()

    def __str__(self):
        return f"{self.currency} {self.value:.2f}"

    def __repr__(self):
        return f"PriceAmount(value={self.value:.2f}, currency='{self.currency}')"

    def __add__(self, other):
        try:
            if not isinstance(other, PriceAmount):
                raise TypeError("Can only add PriceAmount objects.")

            if self.currency != other.currency:
                raise ValueError(
                    f"Cannot add price amounts with different currencies: "
                    f"'{self.currency}' and '{other.currency}'."
                )

            return PriceAmount(self.value + other.value, self.currency)

        except (TypeError, ValueError) as e:
            print(e)
            return None

    def __eq__(self, other):
        if not isinstance(other, PriceAmount):
            return False

        return self.currency == other.currency and self.value == other.value



p1 = PriceAmount(19.99, "usd")
p2 = PriceAmount(10.01, "USD")
p3 = PriceAmount(15.00, "EUR")

print(str(p1))
print(repr(p1))

total = p1 + p2
print(str(total))

print(p1 == PriceAmount(19.99, "USD"))

bad_addition = p1 + p3