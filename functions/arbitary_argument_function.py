def sum(a, b, d, e):
    c = a + b + d + e
    print(c)

def sum_of_all_numbers(*args):
    total = 0
    for i in args:
        # print(i)
        total += i

    print(total)

sum_of_all_numbers(100,200)