import sys
import datetime

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    M1, D1 = sys.stdin.readline().split()
    sys_in.readline()

    try:
        x = datetime.datetime(2019, int(M1), int(D1)+1)
    except:
        print(1)
    else:
        print(0)



if __name__ == '__main__':
    main()