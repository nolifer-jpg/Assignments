def longest_word(str):
    lst = str.split(" ")
    longest = ""
    for word in lst:
        if len(word)>len(longest):
            longest = word
        
    return longest
print(longest_word("Equal max size tie here"))