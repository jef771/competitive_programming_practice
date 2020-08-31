def percentage(arr, n):
    x=sum(arr)
    y=n*100
 
    return "%.12f" %(x*100/y)
 
def main():
    n=int(input())
    d=list(map(int,input().split()))
 
    print(percentage(d,n))
 
 
if __name__ == '__main__':
    main()