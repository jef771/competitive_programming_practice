import sys

def main():
    sys.stdin.readline()

    money = list(map(int, sys.stdin.readline().split()))
    money.sort(reverse = True)

    ans = []
    for i in range(len(money)):
        ans.append(money[i])
        if sum(ans) > sum(money[i+1:]):
            break
    sys.stdout.write(f"{len(ans)}")


if __name__ == '__main__':
    main()