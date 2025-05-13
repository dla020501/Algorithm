def star(n):
    if n == 1:
        return ['***', '* *', '***']
    
    star_list = []
    
    for item in star(n//3): # 1번째 줄
        star_list.append(item * 3)
    for item in star(n//3): # 2번째 줄
        star_list.append(item + ' ' * n + item)
    for item in star(n//3): # 3번쨰 줄
        star_list.append(item * 3)
        
    return star_list


n = int(input())
print('\n'.join(star(n//3)))