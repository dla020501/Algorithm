import sys
input = sys.stdin.readline
import heapq

def main():
    data = []
    for _ in range(int(input())):
        num = int(input())
        if num != 0:
            heapq.heappush(data, num)
        else:
            try:
                print(heapq.heappop(data))
            except:
                print(0)
if __name__ == '__main__':
    main()