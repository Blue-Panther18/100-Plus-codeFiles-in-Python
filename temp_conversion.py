"""
This convert temperature between celsius to fahrenheit..
"""
scale = input("Enter the first letter of Scale used C (celsius) or F (fahrenheit): ")
temp = float(input("Enter the value of measured temperature: "))

if scale == 'c' or scale == 'C':
    convert = (temp * 9 / 5.0) + 32
    print(f"The Fahrenheit equivalent of {temp}C is {convert}F.")

elif scale == 'f' or scale == 'F':
    convert = (temp - 32) * 5 / 9.0
    print(f"The Celsius equivalent of {temp}F is {convert}C.")

else:
    print("Not a recognized scale")