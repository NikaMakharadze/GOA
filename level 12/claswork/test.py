# 1)

age = int(input("Enter your age: "))

if age < 18:
    print("Discount")
else:
    print("Normal Price")

# 2)

num = int(input("Enter your num: "))

if num == 6:
    print("You won house congratulation")
elif num == 30:
    print("You won ticket to Hawaii congratulation")
else:
    print("You won 1$ congratulation")


# 3)

age = int(input("Enter your age: "))
student = True

if age < 18 or student:
    print("discount")
else:
    print("Normal Price")

