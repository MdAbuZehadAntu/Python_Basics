class Outer:


    def __init__(self):
        ## instantiating the 'Inner' class
        self.inner = self.Inner()
        ## instantiating the multilevel 'InnerInner' class
        self.innerinner = self.inner.InnerInner()

    def show_classes(self):
        print("This is Outer class")
        print(inner)

    ## inner class
    class Inner:
        """First Inner Class"""

        def __init__(self):
            ## instantiating the 'InnerInner' class
            self.innerinner = self.InnerInner()

        def show_classes(self):
            print("This is Inner class")
            print(self.innerinner)

        ## multilevel inner class
        class InnerInner:

            def inner_display(self, msg):
                print("This is multilevel InnerInner class")
                print(msg)

        def inner_display(self, msg):
            print("This is Inner class")
            print(msg)

    ## ...
# Let's see how to instantiate the multilevel inner class.

outer = Outer()

inner = outer.Inner()

## this is 'InnerInner' class instance
innerinner = inner.InnerInner() ## innerinner = Outer().Inner().InnerInner()

## let's call its method inner_display
innerinner.inner_display("Just Print It!")