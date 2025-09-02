class MyClass:
    x = 10
    y = 20

    def __init__(self, value1 = 20, value2 = 5):
        self.x = value1
        self.y = value2

    def helloWorld(self):
        print("Hello World")

abc = MyClass(10,20)
xyz = MyClass(300,400)
obj = MyClass()
obj.helloWorld()
print(abc.x, " <====> ", xyz.x)
print(abc.y, " <====> ", xyz.y)
print(obj.x, " <====> ", obj.y)
