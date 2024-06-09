'''
A A A A A
A A A A A
A A A A A
A A A A A
A A A A A
'''

n=int(input("Enetr the range "))
ch=input("Enter the character to print")
for i in range(0,n):
    for j in range(0,n):
        print(ch,end=" ")
    print()