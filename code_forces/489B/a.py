import sys

def main():
    sys.stdin.readline()
    lads = list(map(int, sys.stdin.readline().split()))
    sys.stdin.readline()
    lasses = list(map(int, sys.stdin.readline().split()))
    lads.sort()
    lasses.sort()

    pairs = 0; chosen = []
    for i in min(lads, lasses):
        for k,j in enumerate(max(lads, lasses)):
            if abs(i-j) == 1 and k not in chosen or i-j == 0 and k not in chosen:
                pairs+=1
                chosen.append(k)
                break


    sys.stdout.write(f'{pairs}')

if __name__ == '__main__':
    main()