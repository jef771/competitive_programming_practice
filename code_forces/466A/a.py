import sys


def check_first(n, m, a):
    ans = 0
    while n > 0:
        n-=1
        ans+=a

    return ans


def check_second(n, m, a, b):
    ans = 0
    if b < a:
        while n > 0:            
            n-=m
            ans+=b

        return ans

    else:
        while n > 0:
            if n - m >= 0:            
                n-=m
                ans+=b
            else:
                n-=1
                ans+=a

    return ans

def main():
    n, m, a, b = map(int, sys.stdin.readline().split())

    if m > n and n!=1:
        sys.stdout.write(f'{b}')
    else:
        sys.stdout.write(f'{min(check_first(n,m,a), check_second(n,m,a,b))}')


if __name__ == '__main__':
    main()