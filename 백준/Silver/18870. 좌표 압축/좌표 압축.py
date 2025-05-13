import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    n = int(input())
    data = list(map(int, input().split()))
    sorted_data = sorted(set(data), reverse=True)
    dic = defaultdict(int)
    count = len(sorted_data)  
    for e in sorted_data:
        dic[e] = count - 1
        count -= 1
    for e in data:
        print(dic[e], end=' ')
    

if __name__ == '__main__':
    main()