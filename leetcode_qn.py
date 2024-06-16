#given an array of integers and a number k ,find tht count of distinct element in every window of size k in the array.
#SLIDING WINDOw
'''
def sliding_win(lst,k,n):
    res=[]
    for i in range(0,n-k+1):
        list=[]
        for j in range(i,i+k):   # can use window=lst[i:i+k] and use dc=len(set(list)) instead of using nested loop
            list.append(lst[j])
        dc=len(set(list))
        res.append(dc)
    return res


n=int(input())
lst=[]
for i in range(0,n):
    lst.append(int(input()))
k=int(input())
print(sliding_win(lst,k,n))



an equilibrium index is an index such that the sum of elements of lower indices is equal to the sum of indices at highher indices.
example: [-7,1,5,2,-4,3,0]
output=3
return -1 if no such point exists
'''
'''
def equilibrium(arr):
    lsum=0
    rsum=0
    n=len(arr)
    for i in range(0,n):
        suml=sum(arr[0:i])
        sumr=sum(arr[i+1:n])
        if suml==sumr:
            return i
    return -1

arr=[-7,1,5,2,-4,3,0]
print(equilibrium(arr))


you r given an m X n int grid accoutns where acc[i,j] is the amt of money the ith customer has in j bank. A customers wealth is the
amt of money thy have in all bank accounts.The richest customer is the customer that has the max wealth
inp: [[1,5],[7,3],[3,5]]
outp: 10
'''
'''
def find_richest_customer(accounts):
    max_wealth=0
    for cus in accounts:
        wealth=sum(cus)
        if wealth>max_wealth:
            max_wealth=wealth
    return max_wealth

m=int(input("Enetr the no of customers: "))
n=int(input("Enetr the no of banks :"))

accounts=[]
for i in range(m):
    print(f"Enter the wealth of {i+1}th customer in {n} banks")
    customer_wealth=list(map(int,input().split()))
    accounts.append(customer_wealth)

print(find_richest_customer(accounts))


given an array of size n-1 such tht it only contains distinct integers in the range of 1 to n find the missing element
input: 10
array:[6,1,2,3,8,4,7,9,5]
'''
'''
def missing(arr,n):
    for i in range(0,n-1):
        if arr[i+1]-arr[i]!=1:
            return arr[i]+1
        else:
            continue
    return False
        
n=int(input("Enetr the size of array :"))
#arr=[10,1,2,3,8,4,7,9,5]
arr=list(map(int,input().split()))
arr.sort()
print(missing(arr,n-1))
'''
#or
'''
def missing_num(arr,n):
    total_sum=(n*(n+1))//2
    sum_of_elements=sum(arr)
    missing_number=total_sum-sum_of_elements
    return missing_number

n=int(input("Enetr size of array :"))
arr=list(map(int,input().split()))
print(missing_num(arr,n))
'''

import random

def demonstrate_random_module():
    print("Random module demonstration:")

    #random.random() - returns a random float in the range [0.0,1.0]
    print("\nrandom.random():")
    print(random.random())

    #random.uniform(a,b)-returns a random float in range [a,b]
    print("\nrandom.uniform(1,10):")
    print(random.uniform(1,10))

    #random.randint(a,b)-returns a random int in range[a,b],in
    print("\nrandom.randint(1,10):")
    print(random.randint(1,10))

    #random.randrange(start,stop,step)-returns a randomly selected element frm a non empty
    print("\nrandrange(1,10,2):")
    print(random.randrange(1,10,2))

    #random.choice(seq,weights=None,k=1)
    my_lst=[1,2,3,4,5]
    print("\nrandom.choice([1,2,3,4,5]):")
    print(random.choice(my_lst))

    #random.choices(seq,weights=None,k=1)-returns a list with k randomly int
    print("\nrandom.choices([1,2,3,4,5],k=3:)")
    print(random.choices(my_lst,k=3))

    #random.sample(seq,k)-returns a list of k unique randomly selected 
    print("\nrandom.sample([1,2,3,4,5],k=3:)")
    print(random.sample(my_lst,k=3))

    #randomshuffle(x)-shuffles the sequence x in place
    print("\nrandom.shuffle([1,2,3,4,5]):")
    random.shuffle(my_lst)
    print(my_lst)

    #random.seed((a=None)-initialize the random no generator
    print("\nrandom.seed(10) and random.random():")
    random.seed(10)
    print(random.random())

    #random.getrandbits(k)-returns an integer with k
    print("\nrandom.getrandbits(5):")
    print(random.getrandbits(5))

    #random.guess(mu,sigma)-
    print("random.gauss(0,1):")
    print(random.gauss(0,1))

if __name__=="__main__":
    demonstrate_random_module()


        

