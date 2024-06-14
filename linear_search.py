def linear_search(lst,key,i):
    if i>len(lst)-1:
        return -1
    if lst[i]==key:
        return True
    else:
        return linear_search(lst,key,i+1)

lst=[21,34,21,1,11,73,12]
key=10
print(linear_search(lst,key,0))