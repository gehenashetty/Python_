
n1=int(input("Enetr 1st no "))
n2=int(input("Enter 2nd no "))

temp=0
temp=n1
n1=n2
n2=temp
print(n1,n2)


#swap without third variable
n1=int(input("Enetr 1st no "))
n2=int(input("Enter 2nd no "))
n1,n2=n2,n1
print(n1,n2)

'''another way
a=a+b
b=a-b
a=a-b
'''