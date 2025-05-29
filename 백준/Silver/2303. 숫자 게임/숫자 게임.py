import sys
input = sys.stdin.readline

def main():
    data = (0, 0)
    for num, _ in enumerate(range(int(input())), start=1):
        temp = list(map(int, input().split()))
        maximum = 0
        for i in range(len(temp)-2):
            for j in range(i+1, len(temp)-1):
                for k in range(j+1, len(temp)):
                    tmp = temp[i]+temp[j]+temp[k]
                    if maximum < tmp % 10:
                        maximum = tmp % 10
        if data[1] <= maximum:
            data = (num, maximum)
        
    print(data[0])


if __name__ == '__main__':    
    main()