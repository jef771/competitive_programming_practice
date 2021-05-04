import sys



def get_number(x3):
    temp = ''
    s = str(x3)
    for i in s:
        if i == '.':
            break
        temp+=i

    return temp


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    N = int(sys_in.readline())

    x = N/1.08
    x2 = N//1.08
    x3 = N * 1.08
    x4 = int(get_number(x3))
    print(x)
    print(x2)
    print(x3)
    print(x4)
    if round(x) - x2 >= 1:
        print(f'{x:.0f}')
    elif x4 == N:
        print(x4)
    else:
        print(':(')

if __name__ == '__main__':
    main()