import sys
input = sys.stdin.readline

def main():
    data = set()
    for _ in range(int(input())):
        data.add(input().rstrip())
    sorted_data = sorted(data, key=lambda x: [len(x), x])
    print('\n'.join(sorted_data))

if __name__ == '__main__':
    main()