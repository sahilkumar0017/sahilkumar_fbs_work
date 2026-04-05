price = int(input("Enter ticket price: "))
total = 0

for i in range(5):
    age = int(input("Enter age: "))
    
    if age < 12:
        price = price * 0.7
    elif age > 59:
        price = price * 0.5
    
    total = total + price

print("Total amount:", total)