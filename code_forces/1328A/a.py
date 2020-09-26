import sys

def get_div(a, b):
    if a%b == 0:
        return 0
    else:
        return abs(a%b - b)


def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        sys.stdout.write(f'{get_div(a, b)}\n')


if __name__ == '__main__':
    main()