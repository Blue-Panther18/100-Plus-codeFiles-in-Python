"""
calculates the area of basic shapes.
"""

def shapesArea(shape, *args):
    if shape == "r" or "R" or 's' or 'S':
        return args[0] * args[1]
    elif shape == "C" or 'c':
        return 3.142 * args[0] ** 2
    elif shape == 't' or 'T':
        return 0.5 * args[0] * args[1]
    else:
        return "Invalid shape"
    
shape = input("Enter the shape: ")
if shape == "r" or "R":
    l = float(input("Enter the length: "))
    b = float(input("Enter the breadth: "))
    print("Area of rectangle is: ", shapesArea(shape, l, b))

elif shape == "c" or "C":
    r = float(input("Enter the radius: "))
    print("Area of circle is: ", shapesArea(shape, r))

elif shape == "t" or "T":
    b = float(input("Enter the base: "))
    h = float(input("Enter the height: "))
    print("Area of triangle is: ", shapesArea(shape, b, h))

else:
    print("Invalid shape")