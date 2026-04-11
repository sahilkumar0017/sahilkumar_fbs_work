n = int(input("Enter value of n: "))
count = 0
num = 2

while count < n:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            
            break
    if is_prime:
        print(num, end=" ")
    num += 1