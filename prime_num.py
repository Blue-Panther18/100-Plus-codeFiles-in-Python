'''
Print whether an integer is prime or not.
'''
num = int(input("Enter the integer: "))
count = 0

if num == 0 or num == 1 or num < 0:
    print(f"{num} is not prime.")

else: 
    for x in range(2, num//2):
        if num % x == 0:
            count += 1
    if count == 0:
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")