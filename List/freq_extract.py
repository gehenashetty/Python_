lst=[1,1,1,1,2,2,3,3,3,2,11,11,11,11,19,19,19,19,19]
nwlst=[]
k=4
for i in lst:
    n=i
    count=0
    for i in lst:
        if i==n:
            count+=1
            print(count)
        if count>k and i not in nwlst:
            nwlst.append(i)
print(nwlst)

#or

l=[10,10,22,22,22,11]
nl=[]
k=2
for i in l:
    freq=l.count(i)
    if freq>k and i not in nl:
        nl.append(i)
print(nl)


