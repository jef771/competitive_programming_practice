import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    t = int(sys_in.readline())
    ans = 0

    for _ in range(t):
        w, y, n = map(int, sys_in.readline().split())
        if w%2 == 0 and y%2 != 0:
            while w%2 == 0:
                w/=2
                ans+=2
            if ans >= n:
                sys_out.write('YES\n')
            else:
                sys_out.write('NO\n')
        elif y%2 == 0 and w%2 != 0:
            while y%2 == 0:
                y/=2
                ans+=2
            if ans >= n:
                sys_out.write('YES\n')
            else:
                sys_out.write('NO\n')
        elif w%2 == 0 and y%2 == 0:
            while w%2 == 0 and y%2 == 0:
                y/=2
                w/=2
                ans+=4
                print(ans)
            if ans >= n:
                sys_out.write('YES\n')
            else:
                sys_out.write('NO\n')
        elif n == 1:
            sys_out.write('YES\n')
        else:
            sys_out.write('NO\n')
        ans*=0

            

if __name__ == '__main__':
    main()