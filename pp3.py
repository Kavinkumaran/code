from itertools import combinations
b,m=map(int,input().split())
p=len(str(b))
l1=list(combinations(str(b),p-m))
l1.sort()
print(*l1[0],sep='')
