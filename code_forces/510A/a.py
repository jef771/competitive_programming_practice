import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n, m = map(int, sys_in.readline().split())

    flag = False
    for i in range(n):
        if i%2 != 0:
            if not flag:
                sys_out.write(f"{'.' * (m - 1)}{'#'}\n")
                flag = True
            else:
                sys_out.write(f"{'#'}{'.' * (m - 1)}\n")
                flag = False
        else:
            sys_out.write(f"{'#' * m}\n")


if __name__ == '__main__':
    main()