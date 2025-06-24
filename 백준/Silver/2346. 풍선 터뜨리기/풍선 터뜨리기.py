import sys
from collections import deque

def main():
    """
    풍선 터뜨리기 문제(백준 2346)를 효율적으로 해결하는 코드.
    deque의 rotate 기능을 활용하여 시간 복잡도를 개선합니다.
    """
    n = int(sys.stdin.readline())
    # 풍선의 원래 인덱스(1부터 시작)와 이동 값을 튜플로 묶어 deque에 저장
    # enumerate(..., start=1)을 사용해 1-based 인덱스를 바로 생성
    deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
    
    result = []

    while deq:
        # 1. 현재 풍선을 터뜨린다 (항상 맨 앞의 풍선)
        index, move_val = deq.popleft()
        result.append(index)

        # 모든 풍선을 터뜨렸으면 종료
        if not deq:
            break

        # 2. 다음 풍선으로 이동한다
        if move_val > 0:
            # 양수이면 왼쪽으로 (move_val - 1) 만큼 회전
            # popleft()를 하면서 이미 한 칸 앞으로 이동했기 때문에 -1을 해준다.
            deq.rotate(-(move_val - 1))
        else:
            # 음수이면 오른쪽으로 abs(move_val) 만큼 회전
            # rotate는 음수 값을 받으면 왼쪽으로, 양수 값을 받으면 오른쪽으로 회전한다.
            # 따라서 -move_val을 인자로 주면 된다 (예: move_val = -3 -> rotate(3))
            deq.rotate(-move_val)

    print(*result)

main()