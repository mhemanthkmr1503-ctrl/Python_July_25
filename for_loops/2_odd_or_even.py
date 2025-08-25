list1 = [56,96,78,52,47,69,54]

# number = 5

# if number % 2 == 1:
#     print("Odd")
# else :
#     print("Even")

count_of_even = 0
count_of_odd = 0

for i in list1:
    if i % 2 == 1:
        # print("Odd", i)
        count_of_odd = count_of_odd + 1
    else :
        # print("Even", i)
        count_of_even += 1

print("Even Count :", count_of_even)
print("Odd Count :", count_of_odd)
