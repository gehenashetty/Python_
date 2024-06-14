def list_intersection(l1,l2):
    return list(set(l1) & set(l2))
def list_union(l1,l2):
    return list(set(l1) | set(l2))

l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
print(list_intersection(l1,l2))
print(list_union(l1,l2))