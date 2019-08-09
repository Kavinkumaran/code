n=int(input())
l=list(map(int,input().split()[:n]))
d=[]
for i in range(n):
    if l.count(i)==1:
        d.append(i)

for j in d:
    print(j,end=" ")
