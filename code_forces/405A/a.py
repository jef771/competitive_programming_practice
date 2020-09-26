import sys

def main():
    n = int(sys.stdin.readline())

    cubes = list(map(int, sys.stdin.readline().split()))
    cubes.sort()
    for i in cubes:
        sys.stdout.write(f'{i} ')


if __name__ == '__main__':
    main()