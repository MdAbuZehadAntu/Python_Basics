def fib(n):

    a=0;
    b=1;
    print(a,end="  ")
    print(b,end=" ")

    for i in range(2,n):

        c=a+b;
        if(c>=100):
            break;
        print(c,end=" ");
        a=b;
        b=c;




fib(100);