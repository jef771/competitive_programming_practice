import sys
     
def check_m(x, y):
    max_value = 1
     
    for i in range(1, max(x,y)+1):
        if x%i == 0 and y%i == 0:
            max_value = i
     
    return max_value
     
def main():
    simon, antisimon, n = map(int, sys.stdin.readline().split())
     
    stones = [1] * n; temp = 0; i = 0
    players = (simon, antisimon)
    while stones:
        temp = check_m(players[i], sum(stones))
        while temp != 0:
            stones.pop()
            temp-=1
        i+=1
        if i > 1:
            i*=0
     
    if i == 0:
        sys.stdout.write(f'{1}')
    else:
        sys.stdout.write(f'{0}')
     
     
if __name__ == '__main__':
    main()