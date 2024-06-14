#O(1)
a=[10,20,30,40,50]
index=2
ele=a[index]

print(f"Element at index {index} is {ele}")
'''n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
print(lst)'''

#O(2**n)
#fibonacci number
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input())
result=fib(n)
print(f"the {n}th fibonacci number is: {result}")

