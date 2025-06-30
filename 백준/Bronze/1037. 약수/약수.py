import sys
input = sys.stdin.readline

def main():
    n = int(input())
    data = sorted(list(map(int, input().split())))
    print(data[0] * data[-1])
main()