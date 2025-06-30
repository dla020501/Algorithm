import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    temp1 = 1
    temp2 = 1
    for i in range(k):
        temp1 *= (n-i)
    for i in range(1, k+1):
        temp2 *= i
    print(temp1 // temp2)
main()