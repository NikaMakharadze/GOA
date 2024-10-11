# 1)
def remove_exclamation_marks(s):
    return s.replace('!', '')

# 2)
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return current
    
# 3)
def set_alarm(employed, vacation):
    return True if employed == True and vacation == False else False

# 4)
def get_average(marks):
    return sum(marks) // len(marks)

# 5)
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"
    