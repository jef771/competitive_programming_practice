import sys

def get_ans(ans, K):
    if ans == K:
        return True
    else:
        return False


def check_set(A,B):
    if A.issuperset(B):
        return 1
    else:
        return 0


def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    A = set(map(int, input().split()))
    K = int(input())
    ans = 0
    for i in range(K):
        B = set(map(int, input().split()))
        ans += check_set(A,B)

    print(get_ans(ans,K))



if __name__ == '__main__':
    main()