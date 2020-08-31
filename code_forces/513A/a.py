import sys

def main():
    
    n1,n2,k1,k2 = map(int, sys.stdin.readline().split())

    while True:
        n1-=1
        if n1 == 0:
            sys.stdout.write('Second')
            break
        n2-=1
        if n2 == 0:
            sys.stdout.write('First')
            break

if __name__ == '__main__':
    main()