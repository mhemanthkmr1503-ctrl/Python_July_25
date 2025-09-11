def sum():
    a = 10
    b = 20
    print(a + b)

def paraCalc(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        print(a - b)
    else:
        print("Invalid Operator")


value = paraCalc(15, 60, "-")
print(value)


