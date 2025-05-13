import sys
input = sys.stdin.readline

from collections import defaultdict

def main():
    n = int(input())
    dic = defaultdict(int)
    for e in list(map(int, input().split())):
        dic[e] += 1
    m = int(input())
    for e in list(map(int, input().split())):
        print(1, end=' ') if e in dic else print(0, end=' ')

if __name__ == '__main__':
    main()