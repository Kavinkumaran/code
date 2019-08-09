n=int(input())
d=[]
l=list(map(int,input().split()[:n]))
flag=-1
for i in range(n):
    if l[i]==i:
        d.append(i)
        flag=1
d.sort()
if flag==1:
    for j in d:
        print(j,end='')
elif flag==-1:
    print(-1)
