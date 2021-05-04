import sys

def main():
    
    sys.stdin.readline()

    arr = list(map(int, sys.stdin.readline().split()))

    A = list(map(int, sys.stdin.readline().split()))

    B = list(map(int, sys.stdin.readline().split()))

    print(len(A), len(B))
    ans = 0
    for i,j in zip(A, B):
        if i in arr:
            ans+=1
        if j in arr:
            ans-=1

    sys.stdout.write(f'{ans}')


if __name__ == '__main__':
    main()