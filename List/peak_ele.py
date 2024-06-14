#using Binary Search algo
#list should be sorted for binary search

lst=[10,2,1,3,7,5,6,8]
lst.sort()
def find_peak_ele(lst):
    if not lst:
        return None
    l,r=0,len(lst)-1
    while l<r:
        mid = l+(r-l)//2
        if lst[mid]<lst[mid+1]:
            l=mid+1
        else:
            r=mid
    return lst[l]

print("Peak element is: ",find_peak_ele(lst))