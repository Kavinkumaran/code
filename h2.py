m=int(input())
n=list(map(int,input().split()))[:m]
n.sort()
n.reverse()
if n.count(0)==len(n):
    print("0")
else:
    for i in n:
        print(i,end='')
    
