import sys

def get_lowest(bird_dict, ans):
    lowest_birds = []
    for bird in bird_dict:
        if bird_dict[bird] == ans:
            lowest_birds.append(bird)

    return min(lowest_birds)
            



def get_count(arr):
    counts = {}
    ans = 0
    for birds in arr:
        counts[birds] = counts.get(birds, 0) + 1
        if counts[birds] > ans:
            ans = counts[birds]

    return counts, ans


def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    input()
    birds = tuple(map(int, input().split()))

    bird_dictionary, x = get_count(birds)

    print(get_lowest(bird_dictionary, x))


if __name__ == '__main__':
    main()