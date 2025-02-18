import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
data.sort(key = lambda x:(x[0], x[1]))
for element in data:
    print(' '.join(map(str, element)))