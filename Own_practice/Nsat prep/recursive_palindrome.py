def recursive_palindrome(s):
    if s == "":
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return recursive_palindrome(s[1:-1])
    
print(recursive_palindrome("gello"))