import sys

def main():
    sys.stdin = open('input.txt', 'r')

    s = input()

    lower = []; upper = []; odd = []; even = []

    for i in s:
        if i.isalpha():
            if i.islower():
                lower.append(i)
            else:
                upper.append(i)
        else:
            if int(i) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

    lower.sort(); upper.sort()
    odd.sort(); even.sort()

    ans = "".join(lower+upper+odd+even)

    print(ans)

if __name__ == '__main__':
    main()