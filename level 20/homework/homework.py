# Square(n) Sum

def square_sum(numbers):
    result = 0
    for i in numbers:
        result += i ** 2
    return result

# Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)

# Convert a String to a Number!
def string_to_number(s):
    return int(s)

# Grasshopper - Summation
def summation(num):
    sum = 0
    for number in range(1, num + 1):
        sum += number
    return sum

# Function 1 - hello world

def greet():
    return "hello world!"

# manual_sum

def manual_sum(sum):
    result = 0

    for i in sum:
        result += i
    
    return result

print(manual_sum([1, 2, 3, 4, 10]))

# manual_min

def manual_min(min_index):
    result = min_index[0]

    for i in min_index:
        if i < result:
            result = i
    
    return result 

print(manual_min([3, 1, 4, 1, 5]))

# manual_len

def manual_len(count):
    result = 0
    
    for i in count:
        result += 1
    
    return result

print(manual_len("Hello World!"))