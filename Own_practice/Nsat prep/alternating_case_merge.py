def merge_alternating_case(a, b):
    new_s = ""
    for i in range(len(a)):
        new_s += a[i].lower() + b[i].upper()
    return new_s

print(merge_alternating_case("abc", "xyz"))