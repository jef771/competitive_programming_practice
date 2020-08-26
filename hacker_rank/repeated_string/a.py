import sys
from collections import Counter

def main():
    sys.stdin = open('input.txt', 'r')

    s = list(input())
    n = int(input())

    ans = Counter(s[:n])

    ans2 = n//len(s) * ans['a']

    ans3 = Counter(s[:n%len(s)])

    ans2+=ans3['a']
    
    if 'a' not in ans:
        print(0)
    else:
        print(ans2)


if __name__ == '__main__':
    main()