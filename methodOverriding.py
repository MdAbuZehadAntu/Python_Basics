class A:
    def show(self):
        print("in \"A\" Show");

class B(A):
    def show(self):
        super().show();
        print("in B")

a1=B();
a1.show();