import sys
input = sys.stdin.readline

def make_new_num(n: int):
    if n >= 10:
        a, b = n//10, n%10
    else:
        a, b = 0, n%10
    return b*10 + (a+b)%10

def main():
    n = int(input())   
    temp = n 
    count = 0
    while True:
        temp = make_new_num(temp)
        count += 1
        if temp == n:
            break
    print(count)
    
if __name__ == '__main__':
    main()