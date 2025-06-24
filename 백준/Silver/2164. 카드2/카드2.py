import sys
input = sys.stdin.readline

from collections import deque

def main():
    n = int(input())
    queue = deque()
    for i in range(1, n+1):
        queue.append(i)
    switch = 0
    while len(queue) != 1:
        if switch == 0:
            queue.popleft()
            switch = 1
        else:
            queue.append(queue.popleft())
            switch = 0
    print(*queue)
        
main()