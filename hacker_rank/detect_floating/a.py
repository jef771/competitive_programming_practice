import sys

def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        temp = sys.stdin.readline()
        try:
            if temp != '0':
                float(temp)
                sys.stdout.write('True\n')
            else:
                sys.stdout.write('False\n')
        except:
            sys.stdout.write('False\n')

if __name__ == '__main__':
    main()