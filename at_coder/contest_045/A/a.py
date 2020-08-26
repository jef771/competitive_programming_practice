import sys

def main():
    sys.stdin = open('input.txt', 'r')
    a = int(input())
    b = int(input())
    h = int(input())

    print(int(((a + b) / 2) * h)) 

if __name__ == '__main__':
    main()