n=int(input("Enter number "))
def facto(num):
    fact=1
    while num:
        fact=fact*num
        num-=1
    return fact

res=facto(n)
print("Factorial of ",n,"is ",res)