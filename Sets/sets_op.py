s={"apple","banana","cherry"}
s.add("orange")
print(s)


tropical={"pineapple","mango","papaya"}
s.update(tropical)
print(s)

my_list=["kiwi","custard"]
s.update(my_list)
print(s)

s.remove("banana")
print(s)

s.discard("apple")
print(s)

s.pop()
print(s)

s.clear()
print(s)

#del s
print(s)

s1={'a','b','c',1,2}
s2={1,2,3,4}
s3=s1.union(s2)
print(s3)

#multiple unnion
ss={"John","Gehena"}
s3=s1.union(s2,ss)
print(s3)
s3=s1|s2|ss
print(s3)

s3=s1|s2
print(s3)

#intersection
s4=s1.intersection(s2)
print(s4)
s1.intersection_update(s2)
print(s1)

s4=s1&s2
print((s4))

s1={'a','b','c',1,2}
s2={1,2,3,4}
s5=s1-s2
print(s5)

s5=s1.difference(s2)
print(s5)

s6=s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1)