import sys
from collections import deque
input = sys.stdin.readline
stack = deque()

n = int(input())

for _ in range(n):
    num = int(input())
    
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))