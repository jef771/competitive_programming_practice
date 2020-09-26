import sys


def check_mid(arr, D):
    if len(arr)%2 != 0:
        mid = len(arr)//2
    else:
        mid = len(arr)//2 + 1


    if arr[-1]+D == arr[mid]:
        return True
    else:
        return False

     
def main():
    sys.stdin.readline()
    numbers = list(map(int, sys.stdin.readline().split()))
    numbers = set(numbers)
    if len(numbers) == 1:
        sys.stdout.write('0')
        return
    numbers = list(numbers)

    numbers.sort()
    

    x = numbers.pop()
    D = x - max(numbers)
    numbers.append(x)
    numbers.sort(reverse = True)
    x = numbers.pop()
    D_2 = min(numbers) - x
    numbers.append(x)

     
    if abs(D) == abs(D_2):
        if len(numbers) >= 3:
            flag = check_mid(numbers, abs(D))
            if flag:
                if abs(D)%2 == 0 and abs(D)!=2:
                    if numbers[0] - abs(D) == numbers[-1] + abs(D):
                        sys.stdout.write(f'{abs(D)}')
                    else:
                        sys.stdout.write(f'{abs(D)//2}')
                else:
                    sys.stdout.write(f'{abs(D)}')
            else:
                sys.stdout.write(f'{-1}')
        else:
            if abs(D)%2 == 0:
                sys.stdout.write(f'{abs(D)//2}')
            else:
                sys.stdout.write(f'{abs(D)}')
    else:   
        sys.stdout.write(f'{-1}')
     
     
if __name__ == '__main__':
    main()