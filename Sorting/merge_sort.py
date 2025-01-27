#TC-O(nlogn)
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        sub_array1=arr[:mid]   #for dividing O(logn)
        sub_array2=arr[mid:]
        merge_sort(sub_array1)
        merge_sort(sub_array2)

        i=j=k=0
        while i<len(sub_array1) and j<len(sub_array2):   #for merging/sorting O(n)
            if sub_array1[i]<sub_array2[j]:
                arr[k]=sub_array1[i]
                i+=1
            else:
                arr[k]=sub_array2[j]
                j+=1
            k+=1

        #if either subarray1 or subarray2 is remaining after 1 array finishes
        while i<len(sub_array1):
            arr[k]=sub_array1[i]
            i+=1
            k+=1

        while j<len(sub_array2):
            arr[k]=sub_array2[j]
            j+=1
            k+=1

arr=[10,9,2,4,6,13]
merge_sort(arr)
print(arr)
            