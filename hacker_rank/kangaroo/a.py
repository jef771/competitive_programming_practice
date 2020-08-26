import sys


def get_jump(k1, j1, k2, j2):
    if j1 > j2:
        while k1 < k2:
            k1+=j1
            k2+=j2
        if k1 > k2:
            return 'NO'
        else:
            return 'YES'
    elif j2 > j1:
        while k2 < k1:
            k1+=j1
            k2+=j2
        if k2 > k1:
            return 'NO'
        else:
            return 'YES'
    else:
        if k1 == k2:
            return 'YES'
        else:
            return 'NO'


def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    k1, j1, k2, j2 = map(int, input().split())

    print(get_jump(k1, j1, k2, j2))

if __name__ == '__main__':
    main()