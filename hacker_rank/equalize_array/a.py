import sys
import math
from collections import Counter

def main():

    input()

    numbers = tuple(map(int, input().split()))

    count = Counter(numbers)

    max_int = (sys.maxsize) * (-1)
    for i in count:
        if count[i] > max_int:
            max_int = count[i]
            max_value = i

    ans = 0
    for i in count:
        if i != max_value:
            ans+=count[i]

    print(ans)


if __name__ == '__main__':
    main()
