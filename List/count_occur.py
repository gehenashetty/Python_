def count_occ(lst,n):
    count=0
    for i in lst:
        if i==n:
            count+=1
    return count

lst=[10,11,19,1,20,11,20,12,11,2,11]
n=int(input("Enter the number to chedkc ocurence :"))
print(count_occ(lst,n))