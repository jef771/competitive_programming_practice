s=input()
     
s=s.split(", ")
     
s="".join(s)
     
s=s[1:-1]
     
print(len(set(s)))