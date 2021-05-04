import sys


def solve(x, y, n):
    n-=y
    n//=x

    return x*n + y

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    t = int(sys_in.readline());

    for i in range(t):
        x, y, n = map(int, sys_in.readline().split())
        sys_out.write(f'{solve(x, y, n)}\n')



if __name__ == '__main__':
    main()