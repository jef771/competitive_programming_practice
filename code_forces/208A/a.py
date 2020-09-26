import sys

def main():
    word = sys.stdin.readline().rstrip()

    x = word.split('WUB')
    
    sys.stdout.write(f'{" ".join(x).lstrip().rstrip()}')

if __name__ == '__main__':
    main()