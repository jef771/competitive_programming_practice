# import sys

# def find_sum(arr, l, r, x):
#     ans = 0

#     for i in range(l-1, r):
#         if arr[i] == 0:
#             ans+=x
#         else:
#             ans+=arr[i]

#     return ans


# def main():
#     sys_in = sys.stdin
#     sys_out = sys.stdout


#     n = int(sys_in.readline())
#     numbers = []


#     for _ in range(n):
#         temp = int(sys_in.readline())
#         numbers.append(temp)


#     q = int(sys_in.readline())
#     sys_in.readline()

#     for _ in range(q):
#         l, r, x = map(int, sys_in.readline().split())
#         sys_out.write(f'{find_sum(numbers, l, r, x)}\n')


# if __name__ == '__main__':
#     main()

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    pass
    # Write your code here
    # for i in queries:
    #     l = queries[0]
    #     r = queries[1]
    #     x = queries[2]
    #     return find_sum(numbers, l, r, x)
        
def find_sum(arr, l, r, x):
    ans = 0

    for i in range(l-1, r):
        if arr[i] == 0:
            ans+=x
        else:
            ans+=arr[i]

    return ans    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    print(queries)

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()