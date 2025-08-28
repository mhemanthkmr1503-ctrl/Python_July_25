def sum():
    a = 10
    b = 20
    print(a + b)

def paraCalc(a, b, operator):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    else:
        print("Invalid Operator")


paraCalc(15, 60, "*")

