def div(a,b):
    return a/b;

def smart(div):
    def inner(a,b):
        if(a<b):
            a,b=b,a;
        return div(a,b)
    return inner

div=smart(div)
print(div(2,4));