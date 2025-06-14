def balanced_substrings(s):
    count = 0

    for i in range(len(s)):
        zeros = ones = 0
        for j in range(i, len(s)):
            if s[j] =="0":
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                count +=1
    return count

print(balanced_substrings("0011"))