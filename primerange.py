start=int(input("Enetr starting range "))
end=int(input("Enter ending range "))
prime=0

for g in range(start,end+1):
    count = 0
    a=g//2
    for i in range(2,a+1):
        if g%i==0:
            count+=1
    if count==0:
        prime+=1
        print(g)

print("Total prime numbers ",prime)