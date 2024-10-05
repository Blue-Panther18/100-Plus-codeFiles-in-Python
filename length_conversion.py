"""
convert length from one unit to another.
"""

def lenConverter(value, unit):
    """
        convert length from one unit to another.

        value: the length to be converted.
        unit: the unit to be converted to.
    """
    if unit == "cm":
        return value * 100
    elif unit == "m":
        return value / 100
    elif unit == "km":
        return value / 100000
    else:
        return "Invalid unit."
    
value = float(input("Enter the length: "))
unit = input("Enter the unit: ")

print(lenConverter(value, unit))
