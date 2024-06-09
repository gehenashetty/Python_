'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

n=int(input("Enetr the range "))
for i in range(n):
    for j in range(n):
        if j<=i:
            print(i+1,end=" ")
    print()