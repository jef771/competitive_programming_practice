import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n, k = map(int, sys_in.readline().split())

    members = list(map(int, sys_in.readline().split()))

    team = 0
    for i in members:
        if i + k <= 5:
            team+=1

    sys_out.write(f"{team//3}")


if __name__ == '__main__':
    main()