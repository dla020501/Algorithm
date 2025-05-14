import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    data = defaultdict(int)
    n, m = map(int, input().split())
    for _ in range(n):
        data[input().rstrip()] += 1
    count = 0
    for _ in range(m):
        temp = input().rstrip()        
        if temp in data:
            count += 1
    print(count)

if __name__ == '__main__':
    main()