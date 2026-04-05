gender = input("Enter gender (m/f): ")
age = int(input("Enter age: "))

if (gender == "m" and age >= 21) or (gender == "f" and age >= 18):
    print("Eligible")
else:
    print("Not Eligible")