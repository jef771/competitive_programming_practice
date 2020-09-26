import sys


def play_game(t1, t2):
    if t1[0] == t2[1]:
        return 1
    else:
        return 0

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    teams = []
    for i in range(n):
        temp = tuple(map(int, sys_in.readline().split()))
        teams.append(temp)

    ans = 0
    for i in range(len(teams)):
        for j in range(len(teams)):
            if i != j:
                ans+=play_game(teams[i], teams[j])
    

    sys_out.write(f'{ans}')


if __name__ == '__main__':
    main()