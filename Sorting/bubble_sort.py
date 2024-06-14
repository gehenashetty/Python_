#TC=O(n**2)
def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=[36,11,24,90,2,1,57,38]

print("Sorted array:",bubble_sort(a))