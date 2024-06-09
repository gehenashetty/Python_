'''
* * * * *
  * * * *
    * * *
      * *
        *
'''



n=int(input("Enter a no for rows n colms"))
for i in range(0,n):
    for j in range(0,n):
        if j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()