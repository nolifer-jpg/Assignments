def insert_start(s):
    slist = [s[0]] 
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            slist.append("*")    
        slist.append(s[i+1])    
    return "".join(slist)        

print(insert_start("aaa"))