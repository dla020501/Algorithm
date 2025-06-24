import sys
input = sys.stdin.readline

from collections import deque

def main():
    n = int(input())
    deq = deque()
    for i in map(int, input().split()):
        deq.append(i)
    point = 0
    mem = []
    while True:
        mem.append(point+1)
        next = deq[point]
        deq[point] = 0
        if all(e == 0 for e in deq):
            break
        count = 0
        while count != abs(next):
            if next < 0:
                point -= 1
                if point < 0:
                    point = n + point
            else:
                point = (point + 1) % n
            if deq[point] == 0:
                continue
            else:
                count += 1
    print(*mem)
main()