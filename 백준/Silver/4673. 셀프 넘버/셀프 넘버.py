import sys
from collections import defaultdict

data = defaultdict(int)

def calcTarget(data):
    for i in range(1, 10001):
        temp = str(i)
        result = i
        for j in temp:
            result += int(j)
        data[result] += 1

def main():
    calcTarget(data)
    for i in range(1, 10001):
        if i not in data:
            print(i)

if __name__ == '__main__':
    main()