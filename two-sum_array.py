'''def two(lst,x):
    count=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            sum=lst[i]+lst[j]
            if sum==x:
                return True
            #or
                count+=1
                break
    if count==0:
        return False
    else:
        return True

    return False

lst=[1,-1,2,-2,9,-6]
n=7
x=int(input())
print(two(lst,x))
'''
#another better approach using 2 pointer but list shud be sorted
def two_pointer(lst,x):
    l=0
    r=len(lst)-1
    while l<r:
        if lst[l]+lst[r]==x:
            return True
        elif lst[l]+lst[r]>x:
            r=r-1
        else:
            l+=1
    return False

lst=[1,-1,2,-2,9,-6]
lst.sort()
n=7
x=int(input())
print(two_pointer(lst,x))

