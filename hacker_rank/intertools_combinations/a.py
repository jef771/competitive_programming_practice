import sys
from itertools import combinations

def main():

    sys.stdin = open('input.txt', 'r')

    S, K = input().split()

    for i in range(1, int(K)+1):
        for j in combinations(sorted(S), i):
            print("".join(j))        


if __name__ == '__main__':
    main()