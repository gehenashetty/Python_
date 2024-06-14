def merge_sorted_lists(l1,l2):
    merged_list=[]
    i=j=0
    while i<len(l1) and j<len(l2):
        if l1[i] <l2[j]:
            merged_list.append(l1[i])
            i+=1
        else:
            merged_list.append(l2[j])
            j+=1
    merged_list.extend(l1[i:])
    merged_list.extend(l2[j:])
    return merged_list

l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
print(merge_sorted_lists(l1,l2))
