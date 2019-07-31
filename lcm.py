a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    max1=a
else:
    max1=b
while(True):
    if(max1%a==0 and max1%b==0):
        print("LCM is:",max1)
        break
    max1=max1+1
