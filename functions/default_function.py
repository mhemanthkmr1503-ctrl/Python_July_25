def paraCalc(a = 0, b = 0, operator = "+"):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    else:
        print("Invalid Operator")

paraCalc(15, 100, "-")