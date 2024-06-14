'''s=input("Enter a string :")

#Stirng length
print("Length of string :",len(s))

#Convert uppercase
print("Uppercase:",s.upper())
print(s.isupper())

#Convert lower
print("Lowercawe:",s.lower())
print(s.islower())

#capitalize string and title
print("Capitalized string:",s.capitalize())
print("Capitalize every word:",s.title())

#Count occurences
sub=input("Enetr a substring to count its occurence :")
print("Occurences od",sub,"in the string ",s.count(sub))

#startswith and endswith
prefix=input("Enetr a string to check:")
print("Starts with",prefix,":",s.startswith(prefix))
suffix=input("Enetr a string to check if it ends with it :")
print("Endswith with",suffix,":",s.endswith(suffix))

##replace a string with another
old_string=input("Enetr a string to replace:")
new_string=input("entr a replacement string :")
print("After replacement :",s.replace(old_string,new_string))

#split
delim=input("Enter a delimiter to split string :")
print("Split string:",s.split(delim))

#join a list of substring s into a single string
substrings=input("Enter substrings to join(separated by space):").split()
join_delim=input("enter a delimiter to join the substrings:")
print("joined string;",join_delim.join(substrings))


#strip 
print(s.strip())
print(s.rfind('l')) #finds the pos of last occurence of l  
print(s.rindex('l'))
'''
#formatting 
#print("My name is "+name+"I am "+str(age)+"yaers old"+"I have scored "+str(marks)+"marks") instead
age =36
name=input()
print(f"My nsme is {name},i am {age} years old")