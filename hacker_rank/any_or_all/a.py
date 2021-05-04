import sys


def check_palin(x):
    if str(x) == str(x)[::-1]:
        return 1
    else:
        return 0


def check_positive(x):
    if x < 0:
        return 1
    else:
        return 0

def main():
    sys.stdin = open('input.txt', 'r')

    input()

    numbers = tuple(map(int, input().split()))

    positive = 0; palin = 0

    for i in numbers:
        positive += check_positive(i)
        palin += check_palin(i)

    if positive == 0 and palin > 0:
        print(True)
    else:
        print(False)
        




if __name__ == '__main__':
    main()