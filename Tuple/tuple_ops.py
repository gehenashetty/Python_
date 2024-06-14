#creating a tuple
def create_tuples():
    t1=(1,2,3,4,5,6)
    t2=('a','b','c')
    t3=("app","cod","cam")
    return t1,t2,t3

def access_tuple_items(t1,t2):
    print("Tuple 1: ",t1)
    print("First ele of t1: ",t1[0])
    print("Last ele of t1: ",t1[-1])
    print("tuple2:",t2)
    print("Second ele of t2:",t2[1])
    print("Second last ele of t2:",t2[-2])
    print(t1[0:5])

def unpacking_tuple1(t3):
    (green,yellow,red)=t3
    print(green)
    print(red)
    print(yellow)

def unpacking_tuple2(fruits):
    #using *
    fruits=("apple","banana","cherry","strawberry")
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)


def change_tuples(t1,t2):
    l1=list(t1)
    l2=list(t2)
    l1.append(6)
    l2.remove('c')
    t1=tuple(l1)
    t2=tuple(l2)
    return t1,t2

def loop_through_tuple(t1):
    print("Usinf FOR loop :")
    for i in t1:
        print(i)
    print("Using FOR range:")
    for i in range(0,len(t1)-1):
        print(t1[i])
    print("Using WHILE loop :")
    index=0
    while index<len(t1):
        print(t1[index])
        index+=1

def join_tuples(t1,t2):
    tuple3=t1+t2
    return tuple3

t1,t2,t3=create_tuples()
access_tuple_items(t1,t2)
print()

unpacking_tuple1(t3)
print()

fruits=("Apple","Banana","cherry","strawberry","raspberry")
unpacking_tuple2(fruits)
print()

t1,t2=change_tuples(t1,t2)
print("Afetr making chnages :")
access_tuple_items(t1,t2)
print()

t3=join_tuples(t1,t2)
print("Joined tuples:",t3)

my_tuple=(1,2,3)
another_tuple=tuple([4,5,6])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
com_tuple=my_tuple+another_tuple
print(com_tuple)
repeated_tuple=my_tuple*3
print(repeated_tuple)
print(2 in my_tuple)
print(4 not in my_tuple)
print(len(my_tuple))
for item in my_tuple:
    print(item)
string_to_tuple=tuple("helllo")
print(string_to_tuple)
list_to_tuple=tuple([1,2,3])
print(list_to_tuple)
print(my_tuple.count(11))
print(my_tuple.index(3))

#sort
t=(5,1,11,3,7,2,3)
sorted_tuple=tuple(sorted(t))
print("sorted tuple:",sorted_tuple)
#sort() will change the origonal tuple but sorted() will have one more variable to store

tuple_of_tuples=((1,'apple'),(2,'late'),(3,'dog'))
sorted_tup=sorted(tuple_of_tuples,key=lambda x:x[1]) #sorts based on alphabet 
print("Sorted tuple:",sorted_tup)

#tuple comprehension
square=tuple(x**2 for x in range(1,6))
print(square)

l1=[1,2,3]
l2=['a','b','c']

zipped_tuple=tuple(zip(l1,l2))
print("Zipped tuple:",zipped_tuple)

#named tuple

from collections import namedtuple
import math
#define named tuple
Point=namedtuple('Point',['x','y'])
#create 2 points
p1=Point(1,2)
p2=Point(4,6)
#calculate distance
distance=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
print("Distance btw 2 points:",distance)

#Filter fxn
t=(1,2,3,4,5,6,7,8,9,11)
filter_tuple=tuple(filter(lambda x:x%2!=0,t))  #instead of lambda can use user defined fxn 
print("Filtered tuple ",filter_tuple)

#reduce fxn
from functools import reduce
def add(a,b):
    return a+b

t=(1,2,3,4,5)
reduced_tuple=(reduce(add,t))
print("Result of reducing the tuple:",reduced_tuple)