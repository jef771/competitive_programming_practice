import sys
from collections import Counter

def main():
    
    S = sys.stdin.readline()

    ans = Counter(sorted(S))

    count = 0
    while count < 3:
        max_key = max(ans, key=ans.get)
        sys.stdout.write(f'{max_key} {ans[max_key]}\n')
        del ans[max_key]
        count+=1
    

if __name__ == '__main__':
    main()