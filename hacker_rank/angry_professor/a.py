import sys
from collections import deque

def check_time(deq, thr):
    
    rem_n = [x for x in deq if x > 0]

    for i in rem_n:
        deq.remove(i)

    if len(deq) >= int(thr):
        return 'NO'
    else:
        return 'YES'

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    t = int(input())

    for i in range(t):
        n, k = input().split()
        time = deque(map(int, input().split()))
        print(check_time(time, k))


if __name__ == '__main__':
    main()