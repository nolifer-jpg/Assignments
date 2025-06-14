def is_suffix(word, suffix):
    if suffix in word:
        if word[len(word)-len(suffix):len(word):] == suffix:
            return True
        else: 
            return False
    else:
        return False
    
print(is_suffix("openai", "pen"))