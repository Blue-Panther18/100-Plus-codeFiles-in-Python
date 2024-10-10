'''
It generate the multiplication table of an inputted number from 1 to 12.
'''
def mul_generator(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter the number of table you wish to generate: "))
mul_generator(n)