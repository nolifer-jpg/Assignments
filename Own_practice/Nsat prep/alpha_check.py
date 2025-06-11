def check(s):
    alpha=0
    digits =0
    spc =0
    for char in s:
        if char.isalpha():
            alpha+=1
        elif char.isdigit():
            digits+=1
        else:
            spc += 1
    return f"Alphabet: {alpha}, Digits: {digits}, Special Characters: {spc}"

print(check("Hello@123"))                
