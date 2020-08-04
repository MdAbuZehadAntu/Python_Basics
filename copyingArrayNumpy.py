from numpy import *
# arr1=array([1,2,3,4,5])
# arr2=array([1,9,3,4,5])
# arr=arr1+arr2
# print(sorted(arr,reverse=True))

arr1=array([1,2,3,4,5])
# arr2=arr1.view()
# arr2=arr1
arr2=arr1.copy( )
arr1[1]=99
arr=arr2+arr1

print(arr);

print(arr1,"add : ",id(arr1))
print(arr2,"add : ",id(arr2))
