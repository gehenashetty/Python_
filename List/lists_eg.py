l1=["apple","banana","cherry","mango"]
l2=[10,20,30,40]
l3=[True,False]
l4=list("Jack")
l5=list(("Jack","John"))

x=print(len(l1))
print(type(l1))
print(type(l1[0]))

if "apple" in l1:
    print("Exists")

l1[1]="Kiwi"
print(l1)
l1[1:3]=["Pineapple","Dates","grapes"]
print(l1)

list=["apple","banana","cherry"]
list.insert(2,"watermelon")
print(list)

list.append("chikku")
print(list)

list2=["grape","berry","custard"]
list.extend(list2)
print(list)

list.remove("banana")
print(list)

list2.pop(1)
print(list2)

del list[3]
print(list)

del list2
#print(list2)

list=["apple","mango","cherry"]
list.clear()
print(list)

list3=["gehena","nibha","ssanjana","anay"]
for x in list3:
    print(x)

for  i in range(len(list3)):
    print(list3[i])


list4=["hey","how","are","you"]
i=0
while i<len(list4):
    print(list4[i])
    i+=1


fruits=["apple","cherry","pineapple","grapes","iceapple"]
new=[]

for i in fruits:
    if "a" in i:
        new.append(i)

print(new)

newlst=[i for i in fruits  if "a" in i]
print(newlst)

#Sort
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

num=[1,70,30,50]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

#CUSTOMIZED SORT
#SORT based on how close a number is to 50
def fun(n):
    return abs(n-50)

thislist=[100,50,65,13,46,51,83,11]
thislist.sort(key=fun) #dont pass function call, pass only name and not fun()
print(thislist)

#CAse sensitive

lists=["banana","Orange","Kiwi","cherry","Chhikku"]
lists.sort(key=str.lower) #this sorts the lower case lettrs first
print(lists) 
lists.sort()
print(lists)

def swapp(lst):
    size=len(lst)
    temp=lst[0]
    lst[0]=lst[size-1]
    lst[size-1]=temp
    return lst
    #or
    lst[0],lst[len(lst)-1]=lst[len(lst)-1],lst[0]
    return lst


lst=["gehena","shetty","heaven","bless"]
print(swapp(lst))

#swap based on postions
def swapPositions(lst,pos1,pos2):
    lst[pos1],lst[pos2]=lst[pos2],lst[pos1]
    return lst

    #or

    temp=lst[pos1]
    lst[pos1]=lst[pos2]
    lst[pos2]=temp
    return lst

lst=[11,23,4,67,21]
pos1,pos2=1,3
print(swapPositions(lst,pos1,pos2))

#find sum and average of list

lst=[13,11,57,24,5,39]
sum=0
for i in lst:
    sum=sum+i

print(sum)
avg=sum//len(lst)
print(avg)
print(lst[0])
print(lst[len(lst)-1])

#min and max
lst.sort()
print("Min: ",lst[0]," Max:",lst[len(lst)-1])



#
l1=["apple","banana","cherry","mango"]
l2=[10,20,30,40]
l3=[True,False]
l4=list("Jack")
l5=list(("Jack","John"))

x=print(len(l1))
print(type(l1))
print(type(l1[0]))

if "apple" in l1:
    print("Exists")

l1[1]="Kiwi"
print(l1)
l1[1:3]=["Pineapple","Dates","grapes"]
print(l1)