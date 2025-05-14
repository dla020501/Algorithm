import sys
input = sys.stdin.readline


def main():
    data = input().rstrip()
    n = len(data)
    temp = set()
    for i in range(1, n+1):
        for j in range(n-i+1):
             temp.add(data[j:j+i])
    print(len(temp))

if __name__ == '__main__':
    main()