n=int(input())
arr=[int(x) for x in input().split()]
arr2=[]
for i in arr:
    for j in range(arr.index(i)+1,len(arr)):
        if(i==arr[j]):
            if i not in arr2:
                arr2.append(i)
                break
arr2.sort()
if len(arr2)==0:
    print("unique")
else:
    {print(x,end=" ") for x in arr2}
