import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    name_dict = defaultdict(int)
    num_dict = defaultdict(int)
    
    for num, _ in enumerate(list(range(n)), start=1):
        name = input().rstrip()
        name_dict[name] = num
        num_dict[num] = name
    for _ in range(m):
        entry = input().rstrip()
        if entry in name_dict:
            print(name_dict[entry])
        elif int(entry) in num_dict:
            print(num_dict[int(entry)])

if __name__ == '__main__':
    main()