import sys

def main():
    numbers = list(map(int, sys.stdin.readline().split()))

    value = max(numbers)

    for i in numbers:
        if value != i:
            sys.stdout.write(f'{value - i} ')

if __name__ == '__main__':
    main()