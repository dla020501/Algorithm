import sys
input = sys.stdin.readline

def main():
    n = int(input())
    mem = set()
    count = 0
    for _ in range(n):
        name = input().rstrip()
        if name == "ENTER":
            mem = set()
            continue
        else:
            if name not in mem:
                count += 1
                mem.add(name)
            else:
                continue
    print(count)
main()