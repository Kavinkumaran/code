'''st=input("")
s=[]
for i in range(0,len(st)):
    s.append(st[i])
lll=set(s)
for j in lll:
    print(j,end="")
    print(st.count(j),end="")'''
    
s=input("")
d=[]
for i in range(0,len(s)):
    if s[i] not in d:
        d.append(s[i])
for j in d:
    print(j,end="")
    print(s.count(j),end="")
