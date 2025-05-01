import sys
def input():
    return sys.stdin.readline().rstrip()
def print(object, end='\n'):
    return sys.stdout.write(f"{object}{end}")
N,M = map(int, input().split())
data = []
for i in range(0, N+1):
    data.append(i)
for _ in range(M):
    i,j = map(int, input().split())
    tmp = j
    for k in range(i, (i+j)//2+1):
        data[k], data[tmp] = data[tmp], data[k]
        tmp -= 1
print(' '.join(map(str, data[1::])))
