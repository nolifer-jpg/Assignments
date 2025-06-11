def character_frequency(s):
    s = s.replace(" ", "").lower()
    freq={}
    for char in s:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] =1
    return freq        

print(character_frequency("Hello World"))