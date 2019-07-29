a=input('')
b=""
for i in range(len(a)):
    if (i+1<len(a)):
        if(a[i]!=a[i+1]):
            b=b+a[i]
    else:
        b=b+a[i]
print(b[::-1])        
