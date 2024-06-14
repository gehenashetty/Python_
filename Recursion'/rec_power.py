def pow(n,p):
    if p==0:
        return 1
    #Recurrence relation
    return (n*pow(n,p-1))

n=5
p=3
print(pow(n,p))