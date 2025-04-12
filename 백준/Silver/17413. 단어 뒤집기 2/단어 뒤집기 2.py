import sys
input = sys.stdin.readline

task = input().rstrip()

results = []
flag = 0
temp = []
for token in task:
    if token == '<':        
        results.extend(temp[-1::-1])
        temp = []
        results.append(token)
        flag = 1
        continue
    if token == '>':
        results.append(token)
        flag = 0
        continue
    if flag == 1:
        results.append(token)
        continue    
    if token == ' ':
        results.extend(temp[-1::-1])
        temp = []
        results.append(token)
        continue
    temp.append(token)

results.extend(temp[-1::-1])

print(''.join(map(str, results)))
            