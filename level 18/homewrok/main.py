# 2
print("----------2----------")
int1 = 10
int2 = 5
print(int1 + int2)
# 3
print("----------3----------")
str1 = "hello"
str2 = "world"

combined_str = str1 + " " + str2

print(combined_str) 

# 4
print("----------4----------")
num1 = 10
num2 = 3

result = num1 / num2

print(result)

# When dividing two integers in Python using the / operator the result is a float
# even if both operands are integers

# 5
print("----------5----------")
print(9 + 1)
print(10 - 1)
print(5 * 5)
print(6 / 3)

#6
print("----------6----------")
print(10 + 10 == 10  * 2)
print(7 * 3 != 2 + 2)
print(7 * 3 != 21)
print(9 * 9 == 100 - 100 - 19)

# 7
print("----------7----------")


# 8
print("----------8----------")
a = 5
b = 10
result1 = (a < b) and (b > 0)

x = 15
y = 7
result2 = (x > 20) or (y < 10)

z = -3
result3 = not (z > 0)

name = "Nika"
age = 15
result4 = (name == "Nika") and (age >= 18) 

score = 80
result5 = (score != 100) or (score == 0)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


# 9
print("----------9----------")
for i in range(1, 11):
    print(i)


# 10
print("----------10----------")
listn = [3, 7, 12, 5, 9]

total_sum = 0

for num in listn:
    total_sum += num

print("list's total num is:", total_sum)


# 11
print("----------11----------")
text = "Hello World!"

for i in text:
    print(i)


# 12
print("----------12----------")

number = 1

while number <= 10:
    print(number)
    number += 1 


# 13
print("----------13----------")
number1 = 1

while number1 <= 100:
    if number1 >= 50 and number1 <= 60:
        number1 += 1
        continue

    print(number1)
    number1 += 1

# 14 
print("----------14----------")
number2 = 1

while number2 <= 50:
    print(number2)
    number2 += 1



# 15
print("----------15----------")

def check_divisibility():
    number = int(input("Enter a number: "))
    
    if number % 3 == 0 and number % 5 == 0:
        print(f"The number {number} is divisible both 3 and 5")
    elif number % 3 == 0:
        print(f"The number {number} is divisible only 3")
    elif number % 5 == 0:
        print(f"The number {number} is divisible only 5")
    else:
        print(f"The number {number} is not divisible in 3 or 5")

check_divisibility()

# 16
print("----------16----------")
list1 = [1, 2, 3, 4, 5]

print(int(sum(list1) / len(list1)))

# 17
print("----------17----------")

def strings_upper(string):
    result6 = ""
    num3 = 1
    for i in string:
        if num3 % 2 == 0:
            result6 += i.upper()
        else: 
            result6 += i
        num3 += 1
    print(result6)
strings_upper("makharadze")

print("----------18----------")

def squeared_list(number_list):
    result6 = []
    for i in number_list:
        result6.append(i ** 2)
    return result6
print(squeared_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))