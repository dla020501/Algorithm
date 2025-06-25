import sys
input = sys.stdin.readline

from collections import deque

def main():
    '''
    스택은 fifo이므로 어짜피 넣은 값 그대로 다시 나온다. 따라서 스킵.
    고로 우리는 큐인 경우만 고려하면 된다.
    값을 넣었을 때 나오는 값은 맨 마지막 큐에 들어있던 값과 같다.
    따라서 [큐, 스택, 스택, 큐]이고 초기 값이 [1, 2, 3, 4]이고, 넣는 값이 2, 4, 7이라면,
    큐에 해당하는 것만 고려하면 [1, 4]에 2, 4, 7를 넣는 상황이다.
    이 때 맨 마지막 큐에 들어있던 값을 구해야 하므로
    input 2 -> [2, 1] -> out 4
    input 4 -> [4, 2] -> out 1
    input 7 -> [7, 4] -> out 2
    따라서 답은 4 1 2 가 된다.
    결론은 큐에 해당하는 초기 값 역순으로 가다가 넣는 값 순서대로 가는 식으로 답이 나온다.
    '''
    n = int(input())    
    queuestack_info = []    # 큐에 해당하는 인덱스만 저장
    for index, info in enumerate(map(int, input().split())):
        if info == 0:
            queuestack_info.append(index)
    queuestack = []
    queuestack_init = list(map(int, input().split()))
    # 큐에 들어갈 초기 값 역순으로 저장
    for index in queuestack_info[-1::-1]:
        queuestack.append(queuestack_init[index])
    m = int(input())
    # 넣는 순서대로 저장
    queuestack.extend(list(map(int, input().split())))
    # 앞에서부터 m개 값 뽑기
    print(*queuestack[:m])

main()
    