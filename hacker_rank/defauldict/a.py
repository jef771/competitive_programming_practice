import sys


def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    n_a, n_b = map(int, input().split())

    counts = {}
    for words in range(n_a):
        key = input()
        counts.setdefault(key, [])
        counts[key].append(words+1)

    
    for words in range(n_b):
        key = input()
        if key in counts:
            for i in counts[key]:
                print(i, end=" ")
            print()
        else:
            print('-1')

if __name__ == '__main__':
    main()