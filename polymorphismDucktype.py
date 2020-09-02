class PyCharm:
    def execute(self):
        print("Compiling")
class MyEditor:
    def execute(self):
        print("running")
        print("debugging")


class Laptop:
    def code(self,ide):
        ide.execute()


ide=MyEditor()

lp1=Laptop()
lp1.code(ide)