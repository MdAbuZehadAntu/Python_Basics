class A:
    def __init__(self):
        print("In A's constructor")

    def feature1(self):
        print("Feature 1 in A")
    def feature2(self):
        print("Feature 2 in A")

class B():
    def __init__(self):
        print("In B's constructor")

    def feature3(self):
        print("Feature 3 in B")
    def feature4(self):
        print("Feature 4 in B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C's Constructor")
    def feat(self):
        super().feature4();



#a1=A()
# b1=B()
# b1.feature3()

c1=C()
c1.feat()

# MRO=Method Resolution Order