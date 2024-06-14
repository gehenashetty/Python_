'''
#TC-O(logn)
def bin_search(lst,key):
    l=0
    r=len(lst)-1
    while l<=r:
        m=l+(r-l)//2
        if lst[m]==key:
            return True
        elif lst[m]>key:
            r=m-1
        else:
            l=m+1
    return False

lst=[1,2,3,4,5,6,8]
key=39
print(bin_search(lst,key))
'''
#using recursion TC-O(logn)
def bin_search_recursion(a,target,left,right):
    if left>right:
        return -1
    mid=left+(right-left)//2

    if a[mid]==target:
        return mid
    elif a[mid]<target:
        return bin_search_recursion(a,target,mid+1,right)
    else:
        return bin_search_recursion(a,target,left,mid-1)
    
a=[1,2,3,4,5,6,7,8,9,10]
target=8
result=bin_search_recursion(a,target,0,len(a)-1)

if(result!=-1):
    print(f"Elemnet found at index {result}")
else:
    print(f"Element not found")

