class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print(f"Idnumber:{self.idnumber}")

    
#Child class
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)

    def details(self):
        print(f"my name is {self.name}")
        print(f"idnumber:{self.idnumber}")
        print(f"post:{self.post}")

#creation of object variable or an instance
a=Employee('Rahul',886012,200000,"Intern")
a.display()
a.details()
        
#example for polmorphism and inheritance
class Bird:
    def intro(self):
        print("there are many types of birds ")
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly")  
class ostrich(Bird):
    def flight(self):
        print("they cannot flyy.")

obj_bird=Bird()
obj_spr=sparrow()
obj_ost=ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()
        


#access modifiers
class Super:
    var1=None  #public data member
    _var2=None  #protected data member dnoted by adding one underscore b4 fxn name/variable name
    __var3=None  #private data member  dnoted by adding two underscores b4 fxn name/variable name

    #constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

    #public memner fxn
    def displayPublicMembers(self):
        #accessing public data members
        print("Public data member:",self.var1)
    #protecetd memeber fxn
    def _displayProtectedMembers(self):
        #accessiing proetcted data members
        print("Protectd data member:",self._var2)
    #private member fxn
    def __displayPrivateMembers(self):
        #accessing private members
        print("Private Data Member: ",self.__var3)


    #public member fxn
    def accessPrivateMembers(self):
        #accessing private member fxn
        self.__displayPrivateMembers()

    def accessProtectedMembers(self):
        #accessing protected member fxn
        self._displayProtectedMembers()

#derived class from super
class Sub(Super):
    #constructor
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2, var3)

    #public member fxn
    def accessProtectedMembers(self):
        #accessing protected member fxn of super class
        self._displayProtectedMembers()

    #private cannot be accessed here(in child class )

    
obj=Sub("Hello","all","people!!")
#calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

#object can access protected member
print("Object is accessing protected member:",obj._var2)

#objject cannot access private member,so it will generate attribute
#print(obj.__var3)

