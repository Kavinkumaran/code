def longest(strg1,strg2):
        if(strg1 in strg2):
            return strg1
        else:
            return longest(strg1[0:len(strg1)-1],strg2)
bob = int(input())
vizh= []
for _ in range(0,bob):
    vizh.append(input())
vizh.sort()
print(longest(vizh[0],vizh[bob-1]))

