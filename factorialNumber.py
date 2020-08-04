n=int(input("val : "))


def fact(n):
    c=1;
    for i in range(1,n+1):
        c*=i;
    return c;

print(fact(n));