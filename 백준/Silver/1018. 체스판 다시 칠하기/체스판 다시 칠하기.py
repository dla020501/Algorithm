import sys
N,M = map(int, sys.stdin.readline().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def check(row, col):
    count = 0
    count2 = 0
    color = 'W'
    color2 = 'B'
    for r in range(row, row+8):
        for c in range(col, col+8):
            if data[r][c] != color:
                count += 1
            if data[r][c] != color2:
                count2 += 1
            if c == col+7:
                continue
            color = 'W' if color == 'B' else 'B'
            color2 = 'W' if color == 'B' else 'B'
    return min(count, count2)
        


result = 64

for row in range(N-7):
    for col in range(M-7):
        result = min(result, check(row, col))
sys.stdout.write(f"{result}")