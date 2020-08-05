class Student:

    def __init__(self, name, roll):
        self.lap=self.Laptop("Dell","i5","4gb")
        self.name = name;
        self.roll = roll;


    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand= brand
            self.cpu = cpu
            self.ram = ram
            self.l=self.Inner("ice cream");

        def show(self):
            print(self.brand,self.cpu,self.ram)
            self.l.show();

        class Inner:
            def __init__(self,food):
                self.food=food;
            def show(self):
                print(self.food)




s1 = Student("Antu", 1)
s2 = Student("Bush", 2)



s1.show()

