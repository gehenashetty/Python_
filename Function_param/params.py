#DEfault argument/parameter:in funcn call parameter ws not passed so assign the parameter in the function definition itself
def myFun(x,y=39):
    print("x:",x)
    print("y:",y)

myFun(10)
#Keyworded arguments
def student(firstname,lastname):
    print(firstname,lastname)

student(firstname='Gehena',lastname='Shetty')
student(lastname='Gehena',firstname='Shetty')

#nonkeyworded variable length arguments(argv)
def myfun(*argv):  #* is imp argv u can use any name *a/*guwh
    print(argv)
myfun('Hello','Welcome','to','India')

#keyworded variable length arguments(kwargs)
def myfun1(**kwargs):  #** is imp kwargs u can use any name **a/**guwh
    print(kwargs)
myfun1(a='thnk',b="you",c="byee")

#user defined function 
def cube(x):
    return x*x*x
#LAMBDA function 
cube_v2=lambda x:x*x*x

print(cube(7))
print(cube_v2(5))