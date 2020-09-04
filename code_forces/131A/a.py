import sys

def main():
    s = sys.stdin.readline().rstrip()
    ans = ''

    if s.isupper():
        for i in range(len(s)):
            sys.stdout.write(f"{s[i].lower()}")
    else:
        for i in range(len(s)):
            if i == 0:
                ans+=s[i].upper()
            else:
                if s[i].isupper():
                    ans+=s[i].lower()
                else:
                    sys.stdout.write(f"{s}")
                    return

    sys.stdout.write(f"{ans}")

if __name__ == '__main__':
    main()