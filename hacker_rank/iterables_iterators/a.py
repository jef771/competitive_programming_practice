import sys
from itertools import combinations

def main():
    input()
    arr = sys.stdin.readline().split()
    size = int(sys.stdin.readline())

    index = {}
    for i in range(len(arr)):
        try:
            index[arr[i]]
            index[arr[i]].append(i+1)
        except:
            index[arr[i]] = []
            index[arr[i]].append(i+1)

    arr3 = []
    for i in index:
        arr3.append(str(index[i]))

    arr3 = "".join(arr3)
    arr3 = arr3.replace('[',",")
    arr3 = arr3.replace(']',"")
    arr3 = arr3.replace(" ", "")
    arr3 = arr3.split(",")
    arr3.pop(0)

    ans = [list(x) for x in combinations(arr3, size)]

    count = 0
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if arr[int(ans[i][j])-1] == 'a':
                count+=1
                break
    
    sys.stdout.write("{}".format(count/len(ans)))

if __name__ == '__main__':
    main()