import sys

def fun(s):
    # return True if s is a valid email, else return False
    email_format = (
        '@',
        '.'
    )

    x = s.count('@') + s.count('.')
    if x != 2:
        return False


    username_format = (
        '-',
        '_'
    )



    flag = False
    for i in s:
        if i in email_format:
            flag = True
        if not flag:
            if i.isalpha() or i.isalnum() or i in username_format:
                continue
            else:
                return False
        if flag:
            if i.isalpha() or i in email_format:
                continue
        else:
            return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)