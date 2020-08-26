import sys
from collections import Counter

def main():
    sys.stdin = open('input.txt', 'r')

    input()
    numbers = list(map(int, input().split()))

    n_pairs = Counter(numbers)
    flag = False
    dist = {}
    for i in range(len(numbers)):
        if n_pairs[numbers[i]] == 2:
            flag = True
            try:
                dist[numbers[i]]
            except:
                dist[numbers[i]] = i
            else:
                dist[numbers[i]] -= i

    if not flag:
        print(-1)
        quit()

    ans = []
    for i in dist:
        ans.append(abs(dist[i]))

    print(min(ans))

if __name__ == '__main__':
    main()