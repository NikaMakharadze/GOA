# 2)

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

print(list1)

print(list1[::-1])


# 3)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

first_three = my_list[:3]
print(first_three)

second_three = my_list[3:6]
print(second_three)

third_three = my_list[6:9]
print(third_three)

fourth_three = my_list[9:12]
print(fourth_three)

fifth_three = my_list[12:15]
print(fifth_three)

# 4)

my_list = [10, 20, 30, 40, 50]

my_list[0] = 100
my_list[1] = 200
my_list[2] = 300
my_list[3] = 400
my_list[4] = 500

print([10, 20, 30, 40, 50])
print(my_list)


# 5)

my_list = [10, 20, 30, 40, 50]

print(my_list)

my_list[1:3] = [25, 35]

print(my_list)
