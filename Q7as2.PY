num = int(input("Enter a three-digit number: "))

a=num%10
num=num//10

b=num%10
num=num//10

c=num%10
num=num//10

sum_digits = a + b + c

print("Sum of digits:", sum_digits)