import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def main():
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    gcdd = gcd(a, b)
    print(gcdd * (a//gcdd) * (b//gcdd))

if __name__ == '__main__':
    for _ in range(int(input())):
        main()