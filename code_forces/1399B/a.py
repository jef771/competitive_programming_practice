import sys


def gifts_fixing(candies, oranges, n):

    i = 0
    target_c, target_o = min(candies), min(oranges)
    ans = 0

    while i<n:
        
        temp1 = candies[i] - target_c
        temp2 = oranges[i] - target_o
        ans+=max(temp1, temp2)
                
        i+=1

    return ans


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    t = int(sys_in.readline())

    for i in range(t):
        n = int(sys_in.readline())
        candies = list(map(int, sys_in.readline().split()))
        oranges = list(map(int, sys_in.readline().split()))
        sys_out.write(f'{gifts_fixing(candies, oranges, n)}\n')


if __name__ == '__main__':
    main()
