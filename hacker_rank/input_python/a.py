import sys

def main():
    
    x, y = map(int, sys.stdin.readline().split())

    s = sys.stdin.readline()

    ans = eval(s)

    sys.stdout.write("{}".format(ans == y))
    

if __name__ == '__main__':
    main()