from numpy import *

arr2 = array([

    [1, 2, 3, 6],
    [4, 5, 6, 7]

])

# print(arr2,arr2.size)
# arr1=arr2.flatten()
# print(arr1)
# arr3=arr1.reshape(3,4)
# print(arr3)

m1= matrix('1 2 3; 6 4 5; 1 6 7')
m2= matrix('1 2 3; 6 4 5; 1 6 7')

m=m1*m2
print(m)
