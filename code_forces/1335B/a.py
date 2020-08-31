t=int(input())
latin='abcdefghijklmnopqrstuvwxyz'
 
for i in range(t):
    n,a,b=map(int,input().split())
    string=latin[:b]*n
    print(string[:n])