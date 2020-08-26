import sys


def turn_2(book_pages, n):
    ans = 0;
    for i in range(len(book_pages)-1, 0, -1):
        if n in book_pages[i]:
            break
        else:
            ans+=1

    return ans

def turn_1(book_pages, n):
    ans = 0;
    for i in range(len(book_pages)):
        if n in book_pages[i]:
            break
        else:
            ans+=1

    return ans

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    book = [x for x in range(int(input())+1)]

    n = int(input())

    book_pages = []
    for i in range(0,len(book),2):
        try:
            temp = (book[i], book[i+1])
        except:
            temp = (book[i], 0)
        book_pages.append(temp)

    ans = (
        turn_1(book_pages, n),
        turn_2(book_pages, n)
    )

    print(min(ans))



if __name__ == '__main__':
    main()