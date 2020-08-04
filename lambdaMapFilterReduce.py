from functools import *

lst=[12,62,1,6,77,5]



print(list(map(lambda n : n*2,list(filter(lambda n : n>=5,(list(filter(lambda n : n%2==0,lst)) ))))))

print(reduce(lambda i,n : n+i,(list(map(lambda n : n*2,list(filter(lambda n : n>=5,(list(filter(lambda n : n%2==0,lst)) ))))))))