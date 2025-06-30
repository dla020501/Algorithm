import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    temp1 = 1
    temp2 = 1
    for i in range(n):
        temp1 *= (m-i)
    for i in range(1, n+1):
        temp2 *= i
    print(temp1 // temp2)

for _ in range(int(input())):
    main()