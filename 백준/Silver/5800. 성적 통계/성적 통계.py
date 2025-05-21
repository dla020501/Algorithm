import sys
input = sys.stdin.readline

def main():
    X = 0
    for _ in range(int(input())):
        X += 1
        data = sorted(list(map(int, input().split()))[1:], reverse=True)
        max_ = data[0]
        min_ = data[-1]
        large_gap = 0
        for i in range(len(data)-1):
            if large_gap < data[i] - data[i+1]:
                large_gap = data[i] - data[i+1]
        print(f'Class {X}')
        print(f"Max {max_}, Min {min_}, Largest gap {large_gap}")
        
if __name__ == '__main__':
    main()