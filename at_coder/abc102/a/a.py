import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    N = int(sys_in.readline())

    for i in range(N, sys.maxsize):
        if i%2 == 0 and i%N == 0:
            sys_out.write(f'{i}')
            break

if __name__ == '__main__':
    main()