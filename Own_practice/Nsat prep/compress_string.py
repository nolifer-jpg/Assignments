def compress_string(s):
    freq = {}
    final_s = ""
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char, count in freq.items():
        final_s += char + str(count)