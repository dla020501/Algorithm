import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    
    data = list(range(n))
    result = []
    index = 0
    count = 0
    while not all(element == -1 for element in data):        
        
        if data[index] != -1:
            count += 1
        if count == k:
            count = 0
            result.append(data[index] + 1)
            data[index] = -1

        index = (index + 1) % len(data)
    print('<', end='')
    print(', '.join(map(str, result)), end='')
    print('>')

if __name__ == '__main__':
    main()