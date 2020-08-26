import sys
from collections import Counter

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    input()

    sock = tuple(map(int, input().split()))

    sock = Counter(sock)

    ans = 0; counter = 0
    for k in sock:
        if sock[k] > 1:
            ans = sock[k] % 2
            if ans == 0:
                counter += sock[k]//2
            else:
                counter += (sock[k] - ans)//2

    print(int(counter))



if __name__ == '__main__':
    main()