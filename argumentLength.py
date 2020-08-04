from numpy import *



# def add(*a):
#     c=0;
#
#     for i in a:
#         c+=i;
#     return c
# print(add(1,2,3,4,5,6,7,8,9,10))

# def p(name,age=18):
#     print(age-5)
#
# p("antu")

def person(name,**data):

    print(name)
    print(data)

    for i,j in data.items():
        print("key : "+str(i)+"  data : "+str(j))



person("Antu",age=23,city="Dhaka",id=171092)