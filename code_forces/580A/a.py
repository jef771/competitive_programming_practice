import sys

def main():
    input()
    money = [int(x) for x in sys.stdin.readline().split()]
    count = 0
    ans = []

    for i in range(1,len(money)):
        if money[i-1] <= money[i]:
            count+=1
        else:
            ans.append(count)
            count = 0

    sys.stdout.write('{}'.format(max(ans)+1))

if __name__ == '__main__':
    main()