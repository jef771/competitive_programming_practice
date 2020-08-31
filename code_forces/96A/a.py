import sys

def main():
    players = sys.stdin.readline()

    ans1 = 0; ans2 = 0
    for i in players:
        if ans1 == 7 or ans2 == 7:
            break
        else:
            if i == '1':
                ans1 += 1
                ans2 = 0
            elif i == '0':
                ans2 += 1
                ans1 = 0

    if ans1 == 7 or ans2 == 7:
        sys.stdout.write('YES')
    else:
        sys.stdout.write('NO')


if __name__ == '__main__':
    main()