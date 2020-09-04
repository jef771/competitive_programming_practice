import sys

def main():
    sys.stdin.readline()
    n = tuple(map(int, sys.stdin.readline().split()))

    count = {
             'even': [],
             'odd': []
    }
    for i in range(len(n)):
        if n[i]%2 == 0:
            count['even'].append(i)
        else:
            count['odd'].append(i)

    for i in count:
        if len(count[i]) == 1:
            sys.stdout.write(f'{count[i][0]+1}')


if __name__ == '__main__':
    main()