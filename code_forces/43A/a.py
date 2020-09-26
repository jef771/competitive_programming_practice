import sys

def main():
    n = int(sys.stdin.readline())

    count = {}
    for _ in range(n):
        temp = sys.stdin.readline()
        count[temp] = count.get(temp, 0) + 1


    sys.stdout.write(f'{max(count, key=count.get)}')

if __name__ == '__main__':
    main()