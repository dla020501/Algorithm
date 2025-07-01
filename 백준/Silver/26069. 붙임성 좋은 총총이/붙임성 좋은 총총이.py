import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dancing_person = set()
    for _ in range(n):
        a, b = input().split()
        if (a == "ChongChong" or b == "ChongChong") or (a in dancing_person or b in dancing_person):
            dancing_person.add(a)
            dancing_person.add(b)
        else:
            continue
    print(len(dancing_person))
main()
    