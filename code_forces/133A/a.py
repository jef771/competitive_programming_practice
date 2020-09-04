import sys

def main():
    language = ('H','Q','9')

    p = sys.stdin.readline()

    for i in p:
        if i in language:
            sys.stdout.write('YES')
            return

    sys.stdout.write('NO')

if __name__ == '__main__':
    main()