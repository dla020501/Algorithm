import sys
input = sys.stdin.readline

from collections import defaultdict
def main():
    n = int(input())
    num_count = defaultdict(int)
    data = []
    total = 0
    for _ in range(n):
        num = int(input())
        total += num
        data.append(num)
        num_count[num] += 1
    data.sort()
    sorted_num_count = sorted(num_count.items(), key=lambda x: (x[1], x[0]), reverse=True)
    mem = []
    for key, value in sorted_num_count:
        if value == sorted_num_count[0][1]:
           mem.append(key)
        else:
            break 
    print(round(total / n))
    print(data[(n-1) // 2])
    print(mem[-2] if len(mem) > 1 else mem[0])
    print(data[-1] - data[0])
    
main()
    