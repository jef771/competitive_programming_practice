import sys

def main():
    sys.stdin = open('input.txt', 'r')

    n = int(input())

    soldiers = list(map(int, input().split()))
    ans = 0

    while soldiers[0] != max(soldiers):
        index = soldiers.index(max(soldiers))
        soldiers[index], soldiers[index-1] = soldiers[index-1], soldiers[index]
        ans+=1


    while soldiers[len(soldiers)-1] != min(soldiers):
        soldiers.pop()
        ans+=1


    print(ans)


if __name__ == '__main__':
    main()