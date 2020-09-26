import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    occurrences = tuple(map(int, sys_in.readline().split()))

    pigs = []; ans = 0; s = 1
    for i in occurrences:
        if i > 0:
            s*=i
            while s > 0:
                pigs.append(1)
                s-=1
            s+=1
        else:
            try:
                pigs.pop()
            except:
                ans+=1

    sys_out.write(f'{ans}')

if __name__ == '__main__':
    main()