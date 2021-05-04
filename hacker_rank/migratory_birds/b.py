sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

input()
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1

print(count.index(max(count)))