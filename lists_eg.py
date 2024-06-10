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