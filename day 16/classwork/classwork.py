for i in range(0,200,6):
     print(i)

for i in range(1000, 0, -1):
    print(i)

age = int(input("Enter your age: "))
if age < 18:
    print("50% discount")
else:
    print("No discount")

if age < 18:
    print("50% discount")
elif age == 18:
    print("25% discount")
else:
    print("no discount")

student = input("Are you student: ")
if age < 18:
    print("50% discount")
elif student == "Yes":
    print("50% discount")
else:
    print("No discount")