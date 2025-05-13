

def main(N):
    if N == 1:
        return ['***','* *','***']
    
    result = []    
    
    for row in main(N//3):
        result.append(row*3)
    for row in main(N//3):
        result.append(row+' ' * N+row)
    for row in main(N//3):
        result.append(row*3)
    return result

if __name__ == '__main__':
    N = int(int(input()))    
    print('\n'.join(main(N//3)))