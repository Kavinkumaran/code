e=int(input())
b=list(map(int,input().split()))
p=0
d=[]
for i in range(0,e+1):
    if(b.count(i)>1):
      d.append(i)
if(len(d)==0):
    print("unique")
e=sorted(d)
print(' '.join(map(str,e)))
