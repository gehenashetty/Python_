def print_pattern(n,m):
    if n==0:   #base condition
        return
    for i in range(5,m-1,-1):   #-1 is coz it shud print in reverse/decreasing order 54321.shud start with 5 till 1 so m-1(0-for 1st iteration) so will print till 1
        print(i,end=" ")
    print()
    print_pattern(n-1,m+1)  #recurcise call

n=5   #number of lines
print_pattern(n,1)