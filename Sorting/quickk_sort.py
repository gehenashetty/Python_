def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]

   # left=[x for x in arr if x<pivot]        
   # middle=[x for x in arr if x==pivot]
   # right=[x for x in arr if x>pivot]
   # return quick_sort(left)+middle+quick_sort(right)
    # [exp for loop if cond]

    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x<pivot:
            left.append(x)
    for x in arr:
        if x==pivot:
            middle.append(x)
    for x in arr:
        if x>pivot:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right)

arr=[12,11,13,5,6,7]
print("Given array is :",arr)
sorted_arr=quick_sort(arr)
print("Sorted array is:",sorted_arr)