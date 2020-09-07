class Student:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c;
        elif a!=None and b!=None:
            return a+b;
        else:
            return a+b+c;

s1=Student(45,5);

print(s1.sum(10,20));