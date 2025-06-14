def reverse_even_indices(s):
    even_s = s[::2]
    even_s=  even_s[::-1]
    odd_s = s[1::2]
    final_s = ""
    #print(even_s)
    #print(odd_s)
    k = 0
    j = 0
    for i in range(len(s)):
        if i%2==0:
            
            final_s +=even_s[k]
            k+=1
            #print(final_s)
        else:
            final_s += odd_s[j]
            j+=1
            #print(final_s)
    return final_s
print(reverse_even_indices("abcdef"))
