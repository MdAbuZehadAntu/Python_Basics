
def fact(num):
    if(num==0):
        return 1;
    elif(num<0):
        return;
    else:
        return num*fact(num-1)

print(fact(5));

