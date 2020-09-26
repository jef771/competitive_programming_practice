import sys

def main():
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))

    numbers.sort()

    painted = {}; check = []
    for i in range(n):
        for j in range(i, n):
            if numbers[j]%numbers[i] == 0:
                if numbers[i] not in painted:
                    painted[numbers[i]] = []
                    painted[numbers[i]].append(j)
                else:
                    if j not in painted[numbers[i]]:
                        painted[numbers[i]].append(j)


    count={}
    for i in painted:
        for j in painted[i]:
            if j not in check:
                check.append(j)
                count[i] = count.get(i, 0) + 1

    sys.stdout.write(f'{len(count)}')

if __name__ == '__main__':
    main()