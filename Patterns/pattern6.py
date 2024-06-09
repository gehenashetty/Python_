'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''


n=int(input("Enter a no for rows n colms"))
for i in range(0,n):
    #count = 1
    for j in range(0,n):
        if j<=i:
            #print(count,end=" ")
            #count+=1
            print(j+1,end=" ")
    print()