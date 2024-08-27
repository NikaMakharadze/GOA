# 1)

def say_hello():
    return "Hello, world!"

print(say_hello())

# 2)

def greet_person(name):
    return f"Hello, {name}!"

name = input("Enter your name: ")

print(greet_person(name))

# 3)

def multiply_numbers(a, b):
    return a * b

num1 = 5
num2 = 3
result = multiply_numbers(num1, num2)
print(f"{num1} * {num2} = {result}")

# 4) 

def calculate_sum(a, b, c):
    return a + b + c

num1 = 10
num2 = 7
num3 = 3
result = calculate_sum(num1, num2, num3)
print(f"{num1} + {num2} + {num3} = {result}")

# 5)

def check_adult(age):
    if age >= 18:
        return True
    else:
        return False

user_age = 22
if check_adult(user_age):
    print("you are adult")
else:
    print("you are not adult")

# 6)

def check_passing(score):
    if score >= 80:
        return "Passing"
    else:
        return "Fail"

user_score = 92
result = check_passing(user_score)
print(f"your score {user_score} you {result}")