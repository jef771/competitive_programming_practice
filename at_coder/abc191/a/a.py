import sys


def get_ball(V, T, S, D, A):
    speed = 0
    flag = False
    for i in range(1, 1000):
        speed+=V
        if i>= T and i<=S:
            flag = True
        else:
            flag = False

        if speed > 1000 and D == 1000:
            return 'Yes'
        elif speed >= D:
            if flag:
                return 'No'
            else:
                return 'Yes'


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    V, T, S, D = map(int, sys_in.readline().split())
    A = V
    
    sys_out.write(f'{get_ball(V, T, S, D, A)}')


if __name__ == '__main__':
    main()