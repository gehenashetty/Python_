def power_set(s):
    result=[[]]
    for elem in s:
        result.extend([subset +[elem] for subset in result])
    return [set(subset) for subset in result]

input_set={1,2,3}
powerset=power_set(input_set)
print("Power set:",powerset)

