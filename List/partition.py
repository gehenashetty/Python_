def partition_list(lst,pivot):
    less_than=[x for x in lst if x<pivot]
    greater_than=[x for x in lst if x>pivot]
    equal_to=[x for x in lst if x==pivot]
    return less_than + equal_to + greater_than

lst=[1,2,7,3,8,11,2,8,4,2,10,11,5]
pivot_val=5
print("Partitioned list:",partition_list(lst,pivot_val))