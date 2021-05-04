import sys


def get_room(array, x):
    counts = {}
    for i in array:
        counts[i] = counts.get(i, 0) + 1

    for i in counts:
        if counts[i] == 1:
            return i


def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    K = int(input())
    rooms = tuple(map(int,input().split()))

    print(get_room(rooms, K))

if __name__ == '__main__':
    main()