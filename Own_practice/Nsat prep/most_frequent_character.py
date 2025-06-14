def most_frequent_char(s):
    max_char = ""
    max_count = 0
    for char in set(s):
        max = s.count(char)
        if max > max_count:
            max_count = max
            max_char = char
    return max_char
print(most_frequent_char("aabbc"))            