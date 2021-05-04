import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())
    friends = {}
    temp = list(map(int, sys_in.readline().split()))


    for i in range(n):
        friends[temp[i]] = i+1

    for i in range(n):
        sys_out.write(f'{friends[i+1]} ')
    


if __name__ == '__main__':
    main()