import sys

def cast_void(h, n):
    while n > 0:
        h = h//2 + 10
        n-=1

    return h


def cast_lightning(h, m):
    while m > 0:
        h-=10
        m-=1

    return h

def test_case(x, n, m):
    if x >= 20:
        x = cast_void(x, n)
        x = cast_lightning(x, m)
    else:
        x = cast_lightning(x, m)

    if x>0:
        return 'NO\n'
    else:
        return 'YES\n'

def main():
    n = int(sys.stdin.readline())

    for _ in range(n):
        x, n, m = map(int, sys.stdin.readline().split())
        sys.stdout.write(f'{test_case(x,n,m)}')

if __name__ == '__main__':
    main()