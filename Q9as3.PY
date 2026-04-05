m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))
m4 = int(input("Enter marks4: "))
m5 = int(input("Enter marks5: "))

avg = (m1+m2+m3+m4+m5)/5

if avg >= 60:
    print("First Class")
elif avg >= 50:
    print("Second Class")
else:
    print("Fail")