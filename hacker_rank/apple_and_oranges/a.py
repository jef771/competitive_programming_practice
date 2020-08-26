import sys

def get_orange(o, h1, h2, fruit_array):
    count = 0

    for i in fruit_array:
        ans1 = o + i
        if h2 >= ans1 >= h1:
            count+=1

    return count

def get_apple(a, h1, h2, fruit_array):
    count = 0

    for i in fruit_array:
        ans1 = a + i
        if h2 >= ans1 >= h1:
            count+=1
        
    return count


def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    h1, h2 = map(int,input().split())

    a, o = map(int, input().split())

    input()

    apple_array = map(int,input().split())

    orange_array = map(int,input().split())

    print(get_apple(a, h1, h2, apple_array))
    print(get_orange(o, h1, h2, orange_array))

if __name__ == '__main__':
    main()