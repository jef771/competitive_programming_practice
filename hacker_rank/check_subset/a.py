import sys


def check_set(counts):
    if counts['A'].issubset(counts['B']):
        return True
    else:
        return False

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    T = int(input())

    counts = {
        'A':{},
        'B':{},
    }

    for i in range(T):
        for j in range(2):
            input()
            if j == 0:
                counts['A'] = set(map(int, input().split()))
            else:
                counts['B'] = set(map(int, input().split()))
                print(check_set(counts))


if __name__ == '__main__':
    main()