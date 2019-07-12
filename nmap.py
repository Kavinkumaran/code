a,d=map(str,input().split())
if(len(a)!=len(d)):
    print("no")
else :
    p1=[a.count(i) for i in a]
    p2=[d.count(i) for i in d]
if(p1==p2):
    print("yes")
else:
    print("no")
