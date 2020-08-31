def check_words(arr):    
    if sorted(arr[0]+arr[1]) == sorted(arr[2]):
        return 'YES'
     
    else:
        return 'NO'
     
     
def main():
    print(check_words([tuple(input()) for i in range(3)]))
     
     
if __name__ == '__main__':
    main()