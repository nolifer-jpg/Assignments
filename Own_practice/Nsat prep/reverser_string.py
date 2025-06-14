def main():
    while True:
        try:
            t = int(input())
            break
        except ValueError:
            print("Enter an integer!")
    for _ in range(1,t+1):
        s = input()
        print(reverse_string(s))

def reverse_string(s):
    return s[::-1]


main()           

