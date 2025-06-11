def palindrome(s):
    s = s.replace(" ", "").lower()
    if s[::-1] ==s:
        return "YES"
    else:
        return "NO"
    
print(palindrome("HEllo"))    