import sys

def main():
    sys.stdin = open('input.txt', 'r')

    l, r = map(int, input().split())
    grades = []

    for i in range(r):
        temp = list(map(float, input().split()))
        temp2 = temp[:]
        grades.append(temp2)
        temp.clear()

    grades_dict = {}
    for k in range(len(grades)):
        for j in range(len(grades[k])):
            grades_dict[j+1] = grades_dict.get(j+1, 0) + grades[k][j]

    for i in grades_dict:
        print(grades_dict[i] / r)

if __name__ == '__main__':
    main()