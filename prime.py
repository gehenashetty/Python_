n=int(input("Enter number"))
count=0
a=n//2
for i in range(2,a+1):
    if n%i==0:
        count+=1

if count==0:
    print("Prime")
else:
    print("Not prime")