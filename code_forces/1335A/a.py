import sys

def main():
    # sys.stdin = open('input.txt', 'r')

    n = int(sys.stdin.readline())
     

    for i in range(n):
        x = int(sys.stdin.readline())
        if x == 2:
            y = 0
        elif x%2 != 0:
            y = x//2
        else:
            y = x//2 - 1
        
        sys.stdout.write(str(y))
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()
