import sys

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


    input()

    games = list(map(int, input().split()))
    ans1 = games.pop(0)
    ans2 = ans1

    high = 0;low = 0
    for i in games:
        if i < ans1:
            ans1 = i
            low+=1
        elif i > ans2:
            ans2 = i
            high+=1

    print(high, low)

if __name__ == '__main__':
    main()