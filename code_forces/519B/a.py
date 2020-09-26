import sys
import itertools

def main():
    sys.stdin.readline()

    n = list(map(int, sys.stdin.readline().split()))
    n_2 = list(map(int, sys.stdin.readline().split()))
    n_3 = list(map(int, sys.stdin.readline().split()))

    count = {}; count2 = {}; count3 = {};
    for i, k, j in itertools.zip_longest(n, n_2, n_3, fillvalue = -1):
        count[i] = count.get(i, 0) + 1
        count2[k] = count2.get(k, 0) + 1
        count3[j] = count3.get(j, 0) + 1

    ans = []
    for i in count:
        if i not in count2:
            ans.append(i)
        else:
            if count[i] > count2[i]:
                ans.append(i)

    for i in count:
        if i not in count3:
            if i not in ans:
                ans.append(i)
        else:
            if count[i] > count3[i]:
                if i not in ans:
                    ans.append(i)

    if len(ans) < 2:
        sys.stdout.write(f'{ans[0]}\n{ans[0]}\n')
    else:
        for i in ans:
            sys.stdout.write(f'{i}\n')

if __name__ == '__main__':
    main()