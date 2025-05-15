import sys
input = sys.stdin.readline

from collections import deque

def main(str):
    stack = deque()
    
    for e in str:
        if e == '(' or e == '[':
            stack.append(e)
        elif e == ')':
            try:
                if stack.pop() == '(':
                    continue
                else:
                    print('no')
                    return
            except:
                print('no')
                return      
        elif e == ']':
            try:
                if stack.pop() == '[':
                    continue
                else:
                    print('no')
                    return
            except:
                print('no')
                return    
    if stack:
        print("no")
    else:
        print("yes")   

if __name__ == '__main__':
    while (str := input().rstrip()) != '.':
        main(str)