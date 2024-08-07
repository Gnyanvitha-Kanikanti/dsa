l=list(map(int,input().split()))
max_sum=0
curr_sum=0
neg_ele=0
#first counting the number of negative elements
#if all the elements in the array/list are negative then
#then the maximun subarray will be the whole subarray itself
for i in range(0,len(l)):
    if l[i]<0:
        neg_ele+=1
if neg_ele==len(l):
    print(max(l))
else:
    #iterating throught the full loop
    for i in range(0,len(l)):
        #incrementing the curr_sum full the elements of the loop
        curr_sum+=l[i]
        if curr_sum<0:
            #if curr_sum is less than 0 we are making the curr_sum as 0
            # because we know that there is atleast one positive element in the list
            #so we are making the curr_sum as zero and continuing the calculation from there
            curr_sum=0
        max_sum=max(max_sum,curr_sum)
    print(max_sum)