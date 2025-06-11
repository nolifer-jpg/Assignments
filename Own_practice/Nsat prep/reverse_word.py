def reverse(s):
    s = s.split(" ")
    result =""
    for word in s:
        if len(word)%2==0:
            result += word[::-1] + " "
        else:
            result += word+ " "    
    return result.strip()

print(reverse("this is an awesome test"))         
