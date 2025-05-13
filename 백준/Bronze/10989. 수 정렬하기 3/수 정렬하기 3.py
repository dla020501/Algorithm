import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    data = defaultdict(int)
    for _ in range(int(input())):
        data[int(input())] += 1
    sorted_data = sorted(data.keys())
    for e in sorted_data:
        for _ in range(data[e]):
            print(e)
    

if __name__ == '__main__':
    main()