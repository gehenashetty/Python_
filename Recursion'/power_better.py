def power(n,p):
    if p==1:
        return n
    temp=power(n,p//2)
    if p%2!=0:
        return n*temp*temp
    else:
        return temp*temp

n=int(input())
p=int(input())
po=(power(n,p))
print(po)