a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))
#two sides must be GREATER than the third side
if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")