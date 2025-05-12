import sys
input = sys.stdin.readline
from math import ceil
def main():
    data = []
    for _ in range(n := int(input())):
        data.append(int(input()))        
    data.sort()
    
    outlier = ceil(n * 0.15) if '.5' in str(n*0.15) else round(n * 0.15)
    start_index = outlier
    end_index = n - outlier
    if start_index < end_index:
        if '.5' in str(sum(data[start_index:end_index]) / len(data[start_index:end_index])):
            return ceil(sum(data[start_index:end_index]) / len(data[start_index:end_index]))
        return round(sum(data[start_index:end_index]) / len(data[start_index:end_index]))
    else:
        return 0

if __name__ == '__main__':
    print(main())