# Opposite number

def opposite(number):
  return -number

# Return Negative

def make_negative( number ):
    if number == 0:
        return 0
    elif number < 0:
        return number
    else:
        return -number
    
# Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    return (boolean and "Yes") or "No"

# Sum of positive

def positive_sum(arr):
    res = []
    
    for i in arr:
        if i > 0:
            res.append(i)
            
    return sum(res)

# String repeat

def repeat_str(repeat, string):
    return repeat * string