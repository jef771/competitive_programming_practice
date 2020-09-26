import sys


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    q = int(sys_in.readline())

    count = {}; ans = 0
    for i in range(q):
        s = ''
        count.clear()
        n = int(sys_in.readline())
        ans*=0
        for i in range(n):
            s+=sys_in.readline().rstrip()
        for i in s:
            count[i] = count.get(i, 0) + 1
        for i in count:
            if count[i]%n == 0:
                ans+=1
        if ans == len(count):
            sys_out.write('YES\n')
        else:
            sys_out.write('NO\n')


if __name__ == '__main__':
    main()