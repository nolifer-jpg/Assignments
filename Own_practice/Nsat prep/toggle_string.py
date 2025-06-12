def toggle_string(s):
    vowel = "aeiou"
    for char in s:
        if char in vowel:
            s = s.replace(char, char.upper())
        elif char not in vowel:
            s = s.replace(char, "#")
    return s

print(toggle_string("aeaeae"))            