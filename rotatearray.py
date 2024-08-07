#take list as input from the user
l=list(map(int,input().split()))
#take the number og times we need to rotate the array
k=int(input())
#the number of elements in array
n=len(l)
#we do modulo for reducing the computations
#if the length is 5 and they ask for 6 rotations
#then the output array is same as 1 rotation
#which is length%k
k=k%n
#slicing till the position that need to be rotated
l1=l[:k]
#slicing the leftover list 
l2=l[k:]
#adding them in reverse order
final=l2+l1
print(final)

