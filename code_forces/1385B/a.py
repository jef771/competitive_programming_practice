import sys

def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        x = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        for i in count:
            sys.stdout.write(f'{i} ')
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()