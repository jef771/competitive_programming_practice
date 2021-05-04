import sys

def get_sorted(A):
    for i in range(len(A)):
        if i == K:
            return A[i]


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    N, M = map(int, input().split())

    stats = []
    for i in range(N):
        A = list(map(int, input().split()))
        stats.append(A)

    K = int(input())

    stats.sort(key=get_sorted)

    for i in range(len(stats)):
        for j in range(len(stats[i])):
            print(f'{stats[i][j]} ',end = "")
        print()