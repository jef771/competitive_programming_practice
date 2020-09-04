import sys

def main():
    n = [int(sys.stdin.readline()) for x in range(3)]

    ans2 = n[0]+n[1]*n[2]
    ans3 = n[0]*(n[1]+n[2])
    ans4 = n[0]*n[1]*n[2]
    ans5 = (n[0]+n[1])*n[2]
    ans6 = n[0]+n[1]+n[2]

    sys.stdout.write(f"{max(ans2,ans3,ans4,ans5,ans6)}")


if __name__ == '__main__':
    main()