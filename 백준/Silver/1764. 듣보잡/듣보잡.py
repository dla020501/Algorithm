import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    temp1 = set()
    temp2 = set()
    for _ in range(n):
        temp1.add(input().rstrip())
    for _ in range(m):
        temp2.add(input().rstrip())
    result = sorted(temp1.intersection(temp2))
    print(len(result))
    print('\n'.join(result))

if __name__ == '__main__':
    main()