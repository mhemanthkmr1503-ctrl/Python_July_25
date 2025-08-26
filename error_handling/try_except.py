try:
    a = int(input("Enter a Number 1 :"))
    b = int(input("Enter a Number 2 :"))
    print("Division of A & B is :", a / b)
except Exception as abc:
    print(str(abc))
finally:
    print("Finally Block Exceuted")

a = 10
b = 20
print(a + b)
