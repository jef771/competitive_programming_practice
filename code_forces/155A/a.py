import sys


def main():
    sys.stdin.readline()
    contests = list(map(int, sys.stdin.readline().split()))

    ans = []; new_min = []; new_max = []
    for i in contests:
        ans.append(i)
        new_min.append(min(ans))
        new_max.append(max(ans))


    sys.stdout.write(f'{len(set(new_min))+len(set(new_max))-2}')


if __name__ == '__main__':
    main()