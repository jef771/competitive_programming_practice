import sys

def main():
    a, b = map(int, sys.stdin.readline().split())

    h = 0; count = 0
    while a > 0:
        a-=1
        h+=1
        count+=1
        if count == b:
            a+=1
            count*=0

    sys.stdout.write(f'{h}')


if __name__ == '__main__':
    main()