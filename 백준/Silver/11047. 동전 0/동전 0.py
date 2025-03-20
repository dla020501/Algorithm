import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N, K = map(int, input().split())
    list = []
    
    for _ in range(N):
        list.append(int(input()))
    
    count = 0
    for i in range(-1, -len(list)-1, -1):
        count += K // list[i]
        K = K % list[i]
    return count
        

print(solution())