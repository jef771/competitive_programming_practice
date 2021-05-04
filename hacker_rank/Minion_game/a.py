import sys
from collections import Counter


def get_sub(s, sub_s):
    total = Counter(s[i : i + len(sub_s)] for i in range(len(s)))

    return total[sub_s]

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    s = sys_in.readline().rstrip();
    
    n = len(s)
    voyel = 'AEIOU'

    voyels = []; consonants = []
    for i in range(n):
        temp = s[i]
        if s[i] not in voyel:
            for i in range(i+1, n):
                temp+=s[i]
                if temp not in consonants:
                    consonants.append(temp)
        else:
            for i in range(i+1, n):
                temp+=s[i]
                if temp not in voyels:
                    voyels.append(temp)

    for i in set(list(s)):
        if i not in voyel:
            if i not in consonants:
                consonants.append(i)
        else:
            if i not in voyels:
                voyels.append(i)

    count = {
             'Stuart': 0,
             'Kevin': 0
    }

    ans = 0
    for i in consonants:
        ans+=get_sub(s, i)
        count['Stuart']+=ans
        ans*=0

    for i in voyels:
        ans+=get_sub(s, i)
        count['Kevin']+=ans
        ans*=0
    
    if count['Kevin'] == count['Stuart']:
        sys_out.write('Draw')
    else:
        sys_out.write(f'{max(count, key=count.get)} {count[max(count, key=count.get)]}')
    

if __name__ == '__main__':
    main()