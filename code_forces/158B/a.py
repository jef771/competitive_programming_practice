import sys


def taxi(groups, n):
    i, j, temp = 0, n-1, 0

    ans = 0
    while i <= j:
        temp+=groups[i]+groups[j]
        # print(temp, groups[i], groups[j])
        if temp > 4:
            j-=1
            ans+=1
            temp*=0
        elif temp < 4:
            k = i
            while temp <= 4:
                i+=1
                if i > n-1:
                    return 1
                temp+=groups[i]
            ans+=1
            j-=1
            temp*=0
        else:
            i+=1
            j-=1
            ans+=1
            temp*=0
                
    return ans


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())
    groups = list(map(int, sys_in.readline().split()))

    groups.sort()

    print(taxi(groups,n))


if __name__ == '__main__':
    main()
