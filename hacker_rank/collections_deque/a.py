import sys
from collections import deque

def main():

    d = deque()

    N = int(sys.stdin.readline())

    for i in range(N):
        cmd = sys.stdin.readline().split()
        if len(cmd) > 1:
            if cmd[0] == 'append':
                d.append(cmd[1])
            else:
                d.appendleft(cmd[1])
        else:
            if cmd[0] == 'pop':
                d.pop()
            else:
                d.popleft()

    for i in d:
        sys.stdout.write(f'{i} ')
    

if __name__ == '__main__':
    main()