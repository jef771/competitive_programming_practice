import sys

def check_sum(arr, n):
    ans=[]
    for j in range(3):
        for i in range(n):
            ans.append(arr[i][j])
        if sum(ans) != 0:
            return 'NO'
        ans.clear()

    return 'YES'


def main():
    n = int(sys.stdin.readline())
    vector = []
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        vector.append(temp)

    sys.stdout.write(f'{check_sum(vector, n)}')


if __name__ == '__main__':
    main()