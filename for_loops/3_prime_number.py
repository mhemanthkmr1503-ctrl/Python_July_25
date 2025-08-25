# 1. Get an input from the user
# 2. Need to generate a number from 2 to n-1
# 3. Need to check the n is divisible with generated number.

n = int(input("Enter a Number : "))
flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
        break     

if flag == False:
    print("The given number is not a prime number.")
else:
    print("The given number is prime number.")