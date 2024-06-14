def prod(res_list):
    res=1
    for ele in res_list:
        res=res*ele
    return res

test_list=[11,3,11]
print("The  original list is :",test_list)
res=[]
[res.append(x) for x in test_list if x not in res]
product=prod(res)
print(product)