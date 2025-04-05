import sys
input = sys.stdin.readline

data = []
for _ in range(int(input())):
    w, h = map(int, input().split())
    data.append((w, h))

result = []

for person in data:
    count = 0
    for i in range(len(data)):
        x, y = person
        p, q = data[i]
        
        if x < p and y < q:
            count += 1
    result.append(count+1)

print(*result)