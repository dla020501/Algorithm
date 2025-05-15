import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def main():
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    temp = gcd(a, b)
    print(temp * (a//temp) * (b//temp))
if __name__ == '__main__':
    main()
    