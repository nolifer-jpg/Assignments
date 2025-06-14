def toggle_string(s):
    vowel = "aeiou"
    result=""
    for char in set(s):
        if char in vowel:
            result += char.upper()
        else:
            result += "#"
    return result

print(toggle_string("aeaeae"))            