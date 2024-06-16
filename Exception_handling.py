'''def get_positive_integers():
    while True:
        try:
            num=int (input("Enetr a positive integer: "))
            if num<=0:
                raise ValueError("Not a positive integer!")
            return num
        except ValueError as e:
            print("Error:",e)

positive_integer=get_positive_integers()
print("You entered:",positive_integer)

#CUSTOM EXCEPTION
class MyCustomError(Exception):
    def __init__(self,message):
        self.message=message

try:
    raise MyCustomError("this is a custom error message.")
except MyCustomError as e:
    print("Custom error caught:",e.message)

#2
def access_list_element(lst,index):
    try:
        value=lst[index]
        print("Value at index",index,"is:",value)
    except IndexError:
        print("Erro:Index out of range")

my_list=[1,2,3,4,5]
index=int(input("Enetr an index to access:"))

access_list_element(my_list,index)
'''
#3
def access_dictionary_value(dictionary,key):
    try:
        value=dictionary[key]
        print("Value for key",key,"is:",value)
    except KeyError:
        print("Error:Key not found")
my_dict={'a':1,'b':2,'c':3}
key=input("Enetr a key to access:")
access_dictionary_value(my_dict,key)