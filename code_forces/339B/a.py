import sys

def main():
    n, m = map(int, sys.stdin.readline().split())

    houses = list(map(int, sys.stdin.readline().split()))

    ans = 0; start = 1; aux = 0
    for i in houses:
        if start < i:
            aux = i - start
            ans+=aux
            start+=aux
        elif start > i:
            aux = n - start
            ans+=aux
            start**=0
            ans+=1
            aux = i - start
            ans+=aux
            start+=aux

    sys.stdout.write(f'{ans}')

if __name__ == '__main__':
    main()