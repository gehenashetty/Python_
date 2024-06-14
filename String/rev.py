def rev_string(s,i):
    rstr=' '
    while i>=0:
        rstr=rstr+s[i]
        i-=1
    return rstr

strin=input("enter a string :")
i=len(strin)-1
print("Reversed string:",rev_string(strin,i))

#or
rstring=strin[::-1]
print(rstring)

#palindrome
if rstring==strin:
    print("PAlindrome")
else:
    print("Not palindrome") 