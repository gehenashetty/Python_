l=[10,10,20,30,40,20]
ulist=[]
count=0
'''for i in l:
    if i not in ulist:
        ulist.append(i)
        count+=1
print(ulist)
print(count)'''

#using list comprehension
[ulist.append(i) for i in l if i not in ulist]
print(ulist)