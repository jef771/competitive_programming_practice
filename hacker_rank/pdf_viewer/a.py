import sys
import string

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    values = tuple(map(int, input().split()))

    values_dict = dict(zip(string.ascii_lowercase, values))

    # word = input()

    # ans = []
    # for i in input():
    #     ans.append(values_dict[i])
    ans = [values_dict[x] for x in input()]

    print(max(ans)*len(ans))

    
if __name__ == '__main__':
    main()