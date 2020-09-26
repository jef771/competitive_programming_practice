import sys

def main():
    vowels = 'aoyeui'

    s = list(sys.stdin.readline().lower().rstrip())
    
    # x = 0
    # while x < len(s):
    #     if s[x] in vowels:
    #         s.remove(s[x])
    #     else:
    #         x+=1          

    # x = 0
    # while x < len(s):
    #     s.insert(x,'.')
    #     x+=2

    for i in s:
        if i in vowels:
            continue
        else:
            sys.stdout.write('{}{}'.format(".",i))

    # sys.stdout.write('{}'.format("".join(s)))


if __name__ == '__main__':
    main()