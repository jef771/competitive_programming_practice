import sys
import calendar

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    weekdays = (
        'MONDAY',
        'TUESDAY',
        'WEDNESDAY',
        'THURSDAY',
        'FRIDAY',
        'SATURDAY',
        'SUNDAY')

    month, day, year = map(int, input().split())

    print(weekdays[calendar.weekday(year, month, day)])



if __name__ == '__main__':
    main()