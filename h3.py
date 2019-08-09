n=int(input())
d=[]
l=list(map(int,input().split()[:n]))
for i in range(n):
    if l[i]==i:
        d.append(i)
d.sort()
for j in d:
    print(j,end='')
