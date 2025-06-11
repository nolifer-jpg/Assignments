def alternation_characters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count += 1
    return count        

print(alternation_characters("AABAAB"))