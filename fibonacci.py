"""
This print all the fibonacci sequence within a range.
"""
num = int(input("Enter the value of N: "))
a = 1
b = 1
print(f"{a}, {b}", end="") 
for i in range(num):
    c = a + b
    print(f", {c}", end="")
    a = b
    b = c
print()

