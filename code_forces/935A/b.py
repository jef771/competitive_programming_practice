import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    x = int(sys_in.readline())

    if x%2 == 0 and x != 2:
        sys_out.write('YES')
    else:
        sys_out.write('NO')

if __name__ == '__main__':
    main()