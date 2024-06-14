#not done 

lst=[1,2,3,4,6]
start=int(input())
end=int(input())
newlst=[]

for i in range(start,end+1):
    newlst.append(i)
print(newlst)
lst.sort()
print(lst)
res=False
for j in lst:
    for k in newlst:
        if k==j:
            res=True
print(res)