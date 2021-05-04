import sys


def get_score(array):
    ans = 0
    for k in array:
        if k%2 == 0:
            ans+=2
        else:
            ans+=1

    return ans

def get_numbers(array):
    vowels = (
        'a',
        'e',
        'i',
        'o',
        'u',
        'y'
    )
    counts = []
    temp = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] in vowels:
                temp+=1

        counts.append(temp)
        temp = 0

    return counts


def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    input()

    words = tuple(input().split())

    numbers = get_numbers(words)

    print(get_score(numbers))



if __name__ == '__main__':
    main()