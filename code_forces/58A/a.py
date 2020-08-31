import sys

def main():
    s = sys.stdin.readline().rstrip()
    ans = ''
    target = 'hello'
    x = 0
    y = 0
    count = 0

    while ans != target:
        try:
            s[x]
            if s[x] == target[y] and s[x] not in ans and s[x] != 'l':
                ans+=s[x]
                y+=1
            if s[x] == target[y] and s[x] == 'l' and count < 2:
                ans+=s[x]
                count+=1
                y+=1
            x+=1
        except:
            break

    if target == ans:
        sys.stdout.write('YES')
    else:
        sys.stdout.write('NO')


main()