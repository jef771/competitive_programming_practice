import sys
from collections import Counter
from collections import OrderedDict

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    n, k = input().split()

    h = tuple(map(int, input().split()))
    
    ans = int(k)
    for i in h:
        if i > ans:
            while i > ans:
                ans+=1

    print(ans-int(k))


if __name__ == '__main__':
    main()