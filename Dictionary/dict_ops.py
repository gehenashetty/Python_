#Creating dictionaries 

dict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(dict1)

dict2=dict(name="Gehena",age=21,country="India")
print(dict2)

my_dict={}

my_dict['name']="Gehena"
my_dict['age']=21
my_dict['city']="Mangalore"

print(my_dict)
print(len(my_dict))
print(type(my_dict))

#Accessisng value using keys
print(my_dict['name'])
x=my_dict.keys()
print(x)
y=my_dict.values()
print(y)
z=my_dict.items()
print(z)
m=my_dict.get("city")
print(m)

for x in my_dict:
    print(x)
for x in my_dict:
    print(my_dict[x])

#Iterating over keys
print("Keys:")
for key in my_dict.keys():
    print(key)

#Iterating iver values
print("Values:")
for value in my_dict.values():
    print(value)

#Iteratingn pver kkey value pair
print("Key value pair:")
for key,value in my_dict.items():
    print(key,":",value)

#Checking if a key exists 
if 'name' in my_dict:
    print("name exists in dictionary")
else:
    print("Doesnt exists")

#Modifying 
my_dict["age"]=35
print("Modified age:",my_dict["age"])
#or
my_dict.update({'age':50})
print(my_dict)

#Adding to dictonary
my_dict['color']='fair'
print(my_dict)
#or
my_dict.update({"color2": "dark"})
print(my_dict)


#Removing a key-value pair
removed_value=my_dict.pop('city')
print(removed_value)
print(my_dict)
#or
my_dict.popitem()  #pops last item 
print(my_dict)

my_dict.clear()
print("Dictionary after clearing :",my_dict)

del my_dict

#nested dictioanry
my_fam={
    "child1": {
        "name":"Emil",
        "year":2004
    },
    "child2":{
        "name":"Gehena",
        "year":2002
    },
    "child3":{
        "name":"Ananya",
        "year":2003
    }
}

print(my_fam)
print(my_fam["child2"]["year"])
for x,obj in my_fam.items():
    print(x)
    for y in obj:
        print(y+":",obj[y])

