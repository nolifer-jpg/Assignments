def main():
    t = int(input())
    for _ in range(1, t+1):
        n = int(input())
        print(count_even(n))
        

def count_even(n):
    no_even = 0
    for i in range(1, n+1):
        if i %2 == 0:
            no_even +=1
    return no_even        
        

main()