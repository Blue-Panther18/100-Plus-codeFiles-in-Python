'''
Convert binary number to decimal number.
'''
def bin_to_dec(binary_str):
    decimal_number = int(binary_str, 2)
    return decimal_number

binary_str = input("Enter a binary number: ")
decimal_num = bin_to_dec(binary_str)
print(f"The decimal equivalent of {binary_str} is {decimal_num}.")