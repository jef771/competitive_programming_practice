import sys

def main():
    n, m, p = map(int, sys.stdin.readline().split())

    for i in range(n):
        if i == 0:
            sys.stdout.write(f'[[{sys.stdin.readline().rstrip()}]')
        else:
            sys.stdout.write(f' [{sys.stdin.readline().rstrip()}]')
        sys.stdout.write('\n')

    for i in range(m):
        if i == m-1:
            sys.stdout.write(f' [{sys.stdin.readline().rstrip()}]]')
        else:
            sys.stdout.write(f' [{sys.stdin.readline().rstrip()}]')
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()