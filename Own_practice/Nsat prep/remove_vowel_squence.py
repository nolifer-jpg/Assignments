def remove_middle_vowel(s):
    vowels = "aeiou"
    result =""
    for i in range(len(s)):
        if s[i] in vowels:
            start =  i
            while i< len(s) and s[i] in vowels:
                i+=1
            vowel_group = s[start:i]      
            if start == 0 or i ==len(s):
                result += vowel_group               
              
        else:
            result += s[i]
            i+=1
    
    return result

print(remove_middle_vowel("aeiouxyz"))
