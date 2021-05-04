import sys
from collections import deque

def check_stack(n_d):
    ans = []
    
    while n_d:
        if n_d[0] > n_d[-1]:
            temp = n_d.popleft()
        elif n_d[0] < n_d[-1]:
            temp = n_d.pop()
        else:
            temp = n_d.popleft()
        ans.append(temp)

    
    temp = ans[:]
    temp.sort(reverse = True)
    if ans == temp:
        return 'Yes\n'
    else:
        return 'No\n'


def main():
    T = int(sys.stdin.readline())

    for i in range(T):
        input()
        n = deque(map(int, sys.stdin.readline().split()))
        sys.stdout.write(f'{check_stack(n)}')


if __name__ == '__main__':
    main()