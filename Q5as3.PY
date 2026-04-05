a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))

if a == b == c:
    print("Equilateral")
#all sides are equal
elif a == b or b == c or a == c:
    print("Isosceles")
#two side are equal
else:
    print("Scalene")
#all side are diffrent