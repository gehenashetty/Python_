def counts(s):
    capC=0
    lowC=0
    dig=0
    for i in s:
        if i.isupper():
            capC+=1
        elif i.islower():
            lowC+=1
        elif i.isalnum():
            dig+=1 
    wor=s.split()
    wors=len(wor)
    print(f"The sentence has {wors} words in it.")
    print(f"UpperCase letters : {capC} ")
    print(f"LowerCase letters : {lowC} ")
    return dig

sentence=input()
digs=counts(sentence)
print("No of digits:",digs)