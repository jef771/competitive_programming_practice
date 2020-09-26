import sys

def main():
    n = int(sys.stdin.readline())

    ans = 0
    for i in range(1, n//2+1):
        if n%i == 0:
            ans+=1


    sys.stdout.write(f'{ans}')

if __name__ == '__main__':
    main()