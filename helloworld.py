
# # 14, 12, 14, 5, 4,3,2,1,14,13,12

# # # Append -> It will add the element at last position
# # id(list1).append(100)
# # list1.append(200)
# # print(list1)

# # Insert -> Insert a element at specific position
# # list1.insert(7, 1000)
# # print(list1)



# # Remove -> Remove a element from a list
# # list1.remove(14)
# # print(list1)

# # Pop -> Pop a element from a list using index
# # list1.pop(100)
# # print(list1)

# # Sort -> Sort the List
# # print(list1)
# # list1.sort(reverse = False)
# # print(list1)

# # Reverse -> Reverse the List
# # list1.reverse()
# # print(list1)

# # Count, Index

# # print(list1.index(5))

# # list1 = [1,2,3,4,5] #xahskeovg
# # list2 = list1.copy()
# # list2[2] = 10
# # print((list1)) # [1,2,3,4,5]
# # print((list2)) # [1,2,10,4,5]

# # # Clear
# # list1.clear()
# # print(list1)

# # list1 = [1,2,3,4,5] #xahskeovg
# # list2 = [3,4,5,6,7]

# # list1.extend(list2)
# # print(list1)


# # tuple1 = (1,2,3,4,5,5,5)

# # print(tuple1[4])

# set1 = {1,2,3,4,5,6}

# # add, remove, union, intersection, difference

# # set1.add(-1)
# # set1.add(-5)
# # set1.add(0)
# # set1.remove(-1)
# # print(set1)


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# Outline : get, update, pop, keys, values, items

dict1 = {
    "name" : "Raj",
    "company" : "INFY",
    "age" : 25,
    "isWorking" : True,
    "location" : "Bengaluru"
}
print(dict1)
print(dict1.get("Location", "No Value"))

dict1["name"] = "suresh"
dict1["location"] = "Chennai"


dict1.update(
    {
        "name" : "Suresh",
        "location" : ""
    }
)
print(dict1)
dict1.pop("company")
dict1.pop("name")
dict1.pop("age")


print(dict1.keys())
print(dict1.values())
print(dict1.items())