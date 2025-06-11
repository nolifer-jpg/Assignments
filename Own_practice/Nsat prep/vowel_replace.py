def vowel_replace(s):
    vowels = "aeiou"
    result = ""
    for char in s:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result
