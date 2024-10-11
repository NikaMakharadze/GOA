# 2)

def filter_list(l):
    result = []
    
    for i in l:
        if type(i) == int:
            result.append(i)
    
    return result

# 3)

def get_middle(s):
    s_len = len(s)
    if s_len % 2 == 0:
        return s[s_len // 2 - 1: s_len // 2 + 1]
    return s[s_len // 2]

# 4)

def to_jaden_case(string):
    splited_str = string.split()
    result = ""
    
    for i in splited_str:
        result += i.capitalize() + " "
    return result[:-1]

# 5) 

def manual_min(min_index):
    result = min_index[0]

    for i in min_index:
        if i > result:
            result = i
    
    return result 

print(manual_min([3, 1, 4, 1, 5]))

# 6)

def manual_replace(string1, symbol, replaced_symbol):
    result = ""
    for i in string1:
        if i == symbol:
            result += replaced_symbol
        else:
            result += i
    return result

print(manual_replace("a b c d", " ", "-"))


# 7)

def manual_append(string1):
    return list(string1)

print(manual_append("Hello"))
