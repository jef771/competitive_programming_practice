import sys
import math


def get_max_sum(arr):

    max_sum = -math.inf
    for i in range(1, 5):
        for j in range(1, 5):
            temp = arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j+1]+arr[i+1][j]+arr[i+1][j-1]
            max_sum = max(max_sum, temp)


    return max_sum


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    arr = []

    for _ in range(6):
        temp = list(map(int, sys.stdin.readline().split()))
        arr.append(temp)


    print(get_max_sum(arr))



if __name__ == '__main__':
    main()