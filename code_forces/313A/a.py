import sys

def check_last(n):
    n_str = list(n)
    x = n_str.pop()
    value_1 = int("".join(n_str))
    n_str.pop()
    n_str.append(x)
    value_2 = int("".join(n_str))

    return max(value_1, value_2)

def main():
    n = sys.stdin.readline().rstrip()

    if int(n) > 0:
        sys.stdout.write(f'{n}')
    else:
        sys.stdout.write(f'{check_last(n)}')


if __name__ == '__main__':
    main()