def count_replace(s):
    count= 0
    for char in s:
        if char == " ":
            count +=1
    s = s.replace(char, "-")
    return f"Count: {count}\nReplaced: {s}"

print(count_replace("This is a test"))       