import sys

def main():
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    z = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    sys.stdout.write(f'{[[a,b,c] for a in range(0, x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n]}')

if __name__ == '__main__':
    main()