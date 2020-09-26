import sys
import bisect


def main():
    n = int(sys.stdin.readline())

    shops = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline())
    shops.sort()
    for _ in range(q):
        money = int(sys.stdin.readline())
        sys.stdout.write(f'{bisect.bisect_right(shops, money)}\n')


if __name__ == '__main__':
    main()