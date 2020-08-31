n=input()
x=0
X=input()
X=X[1:]
Y=input()
Y=Y[1:]
     
for i in range(1,int(n)+1):
    if str(i) in X or str(i) in Y:
        x+=1
     
if x==int(n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")