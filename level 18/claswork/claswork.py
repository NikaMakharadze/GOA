str1 = "hello world"
str2 = "HELLO WORLD"
str3 = "hello world"
str4 = "HEllO WoRlD"
str5 = "find the name nika"
str6 = "Nika Makharadze"
str7 = "search for nika"
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
list3 = [10, 20, 30]
list4 = ["a", "b", "d"]
list5 = ["red", "blue", "green", "yellow"]
list6 = ["car", "bike", "car", "plane"]

# Convert all characters in str1 to uppercase
print(str1.upper())  # Output: "HELLO WORLD"

# Convert all characters in str2 to lowercase
print(str2.lower())  # Output: "hello world"

# Capitalize the first character of str3
print(str3.capitalize())  # Output: "Hello World"

# Swap the case of all characters in str4
print(str4.swapcase())  # Output: "heLLo wOrLd"

# Find the first occurrence of "nika" in str5
print(str5.find("nika"))  # Output: 14 ("nika"'s first index is in 14)

# Get the length of str6 or list1
print(len(str6))   # Output: 15
print(len(list1))  # Output: 5

# Find the indexs in srt7 & list2
print(str7.index("nika"))      # Output: 11 ("nika"'s first index is in 11)
print(list2.index("banana"))    # Output: 1

# Append "40" to the end of list3
list3.append(40)
print(list3)  # Output: [10, 20, 30, 40]

# Insert "c" at the 2nd index in list4
list4.insert(2, "c")
print(list4)  # Output: ["a", "b", "c", "d"]

# Remove and return an element from list5 at index 1
removed_item = list5.pop(1)
print(removed_item)  # Output: "blue"
print(list5)         # Output: ["red", "green", "yellow"]

# Remove the first occurrence of "car" from list6
list6.remove("car")
print(list6)  # Output: ["bike", "car", "plane"]
