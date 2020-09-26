import sys

def main():
    t = int(sys.stdin.readline())

    count = {}
    for i in range(t):
        sys.stdin.readline()
        ans = set(map(int, sys.stdin.readline().split()))
        sys.stdout.write(f'{len(ans)}\n')

if __name__ == '__main__':
    main()