import sys


def main():
    red, blue = map(int, sys.stdin.readline().split())

    count = 0
    while red > 0 and blue > 0:
        red-=1
        blue-=1
        count+=1

    sys.stdout.write(f'{count} ')

    count*=0
    max_ele = max(red,blue)
    while max_ele > 0 and max_ele >= 2:
        max_ele-=2
        count+=1

    sys.stdout.write(f'{count}')


if __name__ == '__main__':
    main()