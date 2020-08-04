from calcModule import *

a,b=7,14;

def smart(sub,div):
    def inner(a,b):
        if (a < b):
            a,b=b,a;
        return sub(a,b),div(a,b)
    return inner,inner;


sub,div=smart(sub,div);

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))

