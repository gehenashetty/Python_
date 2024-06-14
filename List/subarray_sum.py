#iMPORTANT SUM***

def largest_subarray_sum(lst):
    max_sum=curr_sum=lst[0]

    for num in lst[1:]:
        curr_sum=max(num,curr_sum+num)
        max_sum=max(max_sum,curr_sum)
    return max_sum

lst=[-2,1,-3,4,-6,2,1,-5,4]

print(largest_subarray_sum(lst))