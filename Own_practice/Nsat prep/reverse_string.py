def recursive_reverse_string(s):
    if s == "":
        return s
    else:
        return recursive_reverse_string(s[1:])+ s[0]
        
print(recursive_reverse_string("hellow"))