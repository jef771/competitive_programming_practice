n=int(input());x=0;y=0
     
while n!=0:
   	while n>=100:
   		x=n//100
   		y+=x
   		n%=100
   	while n>=20:
   		x=n//20
   		y+=x
   		n%=20
   	while n>=10: 
   		x=n//10
   		y+=x
   		n%=10
   	while n>=5:
   		x=n//5
   		y+=x
   		n%=5
   	while n>=1:
   		n-=1
   		y+=1
     
     
print(y)
