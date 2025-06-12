def BFS(x, y):
    while dq:
        temp = dq.popleft()
        if (not board[temp[0]][temp[1]]):
            continue
        jump = board[temp[0]][temp[1]]
        board[temp[0]][temp[1]] = 0
        X, Y = temp[0]+jump, temp[1]+jump
        if (x <= X < N):
            dq.append((X, temp[1]))
        if (y <= Y < N):
            dq.append((temp[0], Y))

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dq = deque([[0, 0]])
BFS(0, 0)

print('HaruHaru' if not board[-1][-1] else 'Hing')