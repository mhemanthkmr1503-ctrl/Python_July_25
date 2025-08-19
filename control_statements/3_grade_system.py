# Problem : Identify the grade based on the mark
# Input : Int
# Output : String

# Business Logic:
# 91 - 100 : O
# 81 - 90 : A+
# 71 - 80 : A
# 61 - 70 : B+
# 50 - 60 : B
# Below 50 : U
# 100 > : Invalid Mark
# Below 0 : Invalid Mark (Done)

mark = int(input("Enter a mark :"))

if (mark > 100) or (mark < 0):
    print("Invalid Mark")
elif mark >= 91 and mark <= 100:
    print("Grade O")
elif mark >= 81 and mark <= 90:
    print("Grade A+")
elif mark >= 71 and mark <= 80:
    print("Grade A")
elif mark >= 61 and mark <= 70:
    print("Grade B+")
elif mark >= 50 and mark <= 60:
    print("Grade B")
else:
    print("U")