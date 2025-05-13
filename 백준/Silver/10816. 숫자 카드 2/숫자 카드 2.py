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
        print(dic[e], end=' ')

if __name__ == '__main__':
    main()