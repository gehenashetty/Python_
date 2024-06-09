
def happy(num):
    sum=0
    while num:
        digit=num%10
        sum=sum+digit**2
        num=num//10
    return sum

num=int(input())
res=num
sum=0

while(num!=4 and num!=1):
    num=happy(num)

if num==1:
    print("True")
elif(num==4):
    print("False")

#happy number for all will either give 1 or 4 only at the end so take this condition


