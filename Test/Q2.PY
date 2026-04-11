n = int(input("Enter value of n: "))
fact = 1
sum_series = 0

for i in range(1, n + 1):
    fact = fact * i   # factorial
    sum_series +=fact

print("Sum of series =", sum_series)