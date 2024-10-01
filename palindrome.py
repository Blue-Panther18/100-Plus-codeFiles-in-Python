"""
This checks if a number is palindrome or not.
"""
num = int(input("Enter a number: "))
q = num
result = 0

while(q != 0):
    rem = q % 10
    q //= 10
    result = (result*10) + rem


if(result == num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")