import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    bottom = b*d
    top = a*d + b*c
    
    temp = gcd(bottom, top)
    print(top//temp, bottom//temp)

if __name__ == '__main__':
    main()
    