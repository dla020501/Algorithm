import sys
input = sys.stdin.readline

def main():
    N = int(input())
    target = int(input())
    grid = [[0]*N for _ in range(N)]
    
    count = 0   # 앞으로 간 횟수 세는 용
    go = 1      # 몇칸 앞으로 가야하는지 세는 용
    cur = 1     # grid에 쓰는 용
    direct_num = 0  # 방향 정하는 용, 인덱스
    direction = [(-1,0), (0,1), (1,0), (0,-1)]  # 방향 정하는 용
    
    current = (N//2, N//2)    # 시작하는 지점
    grid[N//2][N//2] = 1
        
    while 1:
        for _ in range(2):  # go만큼 앞으로 가는걸 2번씩 한다
            for _ in range(go): # go만큼 1칸씩 이동                
                x, y = current
                if cur == target:
                    result = (x+1, y+1)   # 1-based
                if cur == N**2:
                    for row in grid:
                        print(' '.join(str(x) for x in row))
                    print(*result)
                    return
                
                nxt_x, nxt_y = direction[direct_num]
                next_x, next_y = x+nxt_x, y + nxt_y
                cur += 1
                grid[next_x][next_y] = cur                                
                current = (next_x, next_y)
                
            direct_num = (direct_num + 1) % 4
                
        go += 1
        
if __name__ == '__main__':
    main()