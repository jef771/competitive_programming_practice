import sys

def main():
    n = int(sys.stdin.readline())

    count = {}; ans = ''
    for i in range(n):
        str = sys.stdin.readline().rstrip()
        count[str] = count.get(str, 0) + 1
        if count[str]-1 == 0:
            sys.stdout.write('OK\n')
        else:
            sys.stdout.write(f'{str}{count[str]-1}\n')

if __name__ == '__main__':
    main()