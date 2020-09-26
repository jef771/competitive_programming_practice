import sys


def get_value(k, r):
    temp = k
    for i in range(1, 1000000000000):
        temp*=i
        # print(temp, r, i)
        if (temp-r) % 10 == 0 or temp%10 == 0:
            return i
        temp*=0
        temp+=k


def check(k, r):
    if k-r % 10 == 0:
       return True
    else:
        return False 


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    k, r = map(int, sys_in.readline().split())

    if check(k, r):
        sys_out.write('1')
    else:
        ans = get_value(k, r)
        sys_out.write(f'{ans}')

if __name__ == '__main__':
    main()