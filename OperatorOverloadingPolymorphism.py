a=5;
b=6;

print(int.__add__(a,b));

class Student:
    def __init__(self,n1,n2):
        self.n1=n1;
        self.n2=n2;
    def __add__(self, other):
        n1=self.n1+other.n1;
        n2=self.n2+other.n2;
        s3=Student(n1,n2);
        return s3;

    def __gt__(self, other):
        m1=self.n1+self.n2;
        m2=other.n1+other.n2;
        if m1>m2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(s1.n1,s1.n2);

s1=Student(100,20);
s2=Student(59,1);

s3=s1+s2;
print(s3.n1);

if s1>s2:
    print("S1 wins");
else:
    print("S2 wins");

s=9;
print(s.__str__());

print(s1);