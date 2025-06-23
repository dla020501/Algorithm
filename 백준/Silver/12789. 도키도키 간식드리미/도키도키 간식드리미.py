import sys
input = sys.stdin.readline

def main():
    n = int(input())
    data = list(map(int, input().split()))
    
    start = 1
    mem = []
    stack = []
    index = 0
    while True:
        if stack and start == stack[-1]:
            mem.append(stack.pop())
            start += 1
            continue
        if index == n:
            break
        e = data[index]
        
        if e == start:
            mem.append(e)
            start += 1
            index += 1
        else:
            stack.append(e)
            index += 1
    
    while stack:
        if start == stack[-1]:
            mem.append(stack.pop())
            start += 1
        else:
            print("Sad")
            exit()
    print("Nice")
        
main()