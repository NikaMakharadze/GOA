# 2)

def sum_numbers_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

start_value = 1
end_value = 10
result = sum_numbers_in_range(start_value, end_value)
print(f"{start_value} {end_value} {result}")


# 3)

def introduce_myself(name, surname, age, institution):
    introduction = f"My name is {name}, my surname is {surname}, I am {age} years old, and I study at {institution}."
    return introduction

my_name = "Nika"
my_surname = "Makharadze"
my_age = 15
my_institution = "GOA"
my_bio = introduce_myself(my_name, my_surname, my_age, my_institution)
print(my_bio)

# 4)

def greet_person(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

user_first_name = "Nika"
user_last_name = "Makharadze"
greeting = greet_person(user_first_name, user_last_name)
print(greeting)

# 5)

def calculate_sum_and_assign(a, b):
    total = a + b
    return total

num1 = 10
num2 = 7
result_sum = calculate_sum_and_assign(num1, num2)
print(f"{num1} + {num2} = {result_sum}")

my_variable = result_sum
print(f"{my_variable}")

# 6)

def calculate_product_and_assign(a, b, c):
    product = a * b * c
    return product

num1 = 2
num2 = 3
num3 = 4
result_product = calculate_product_and_assign(num1, num2, num3)
print(f"{num1} * {num2} * {num3} = {result_product}")

my_variable = result_product
print(f"{my_variable}")

# 7)

def print_food_(food_list):
    for food in food_list:
        print(food)

food_list = ["Pizza", "Burger", "Ice Cream", "Potato"]
print_food_(food_list)
