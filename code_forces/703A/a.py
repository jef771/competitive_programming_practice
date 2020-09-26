import sys


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    count = {
                'Mishka': 0,
                'Chris': 0
    }

    for i in range(n):
        m, c = map(int, sys_in.readline().split())
        if m > c:
            count['Mishka']+=1
        elif c > m:
            count['Chris']+=1


    if count['Mishka'] == count['Chris']:
        sys_out.write('Friendship is magic!^^')
    else:
        sys_out.write(f'{max(count, key=count.get)}')

if __name__ == '__main__':
    main()