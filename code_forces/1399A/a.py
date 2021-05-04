import sys
import collections


def remove_smallest(n, nums):

    while len(nums) > 1:
        i = nums[0]
        j = nums[1]

        temp = abs(i - j)

        if temp <= 1:
            nums.popleft()
        else:
            return 'NO'

    return 'YES'


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    t = int(sys_in.readline())

    for i in range(t):
        n = int(sys_in.readline())
        nums = list(map(int, sys_in.readline().split()))
        nums.sort()
        nums = collections.deque(nums)
        sys_out.write(f'{remove_smallest(n, nums)}\n')


if __name__ == '__main__':
    main()
