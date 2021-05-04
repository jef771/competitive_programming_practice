import sys


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    t = int(sys_in.readline())

    count = {}
    for _ in range(t):
        n = int(sys_in.readline())
        nums = list(map(int, sys_in.readline().split()))
        for j in range(n):
            if nums[j] not in count:
                count[nums[j]] = [j]
            else:
                count[nums[j]].append(j)

        for k in set(nums):
            if len(count[k]) == 1:
                sys_out.write(f'{count[k][0]+1}\n')

        count.clear()
     



if __name__ == '__main__':
    main()