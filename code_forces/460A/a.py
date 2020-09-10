import sys

def main():
    n, m = map(int, sys.stdin.readline().split())

    d = 0; count = 0
    while n > 0:
        d+=1
        n-=1
        if d%m == 0:
            n+=1
        count+=1

    sys.stdout.write(f'{count}')


if __name__ == '__main__':
    main()