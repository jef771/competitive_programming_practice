import sys
from collections import deque

def main():
    sys.stdin = open('input.txt', 'r')

    players = {
        'a': None,
        'b': None,
        'c': None
    }

    for i in players:
        players[i] = deque(tuple(input()))

    card = 'a'
    while players[card]:
        card = players[card].popleft()

    print(card.upper())


if __name__ == '__main__':
    main()