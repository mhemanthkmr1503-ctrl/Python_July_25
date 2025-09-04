"""
Method overridind -> In python there is no method overriding
int sum(int a, int b) 
{
    return a + b;
}

float sum(float a, float b) 
{
    return a + b;
}

float sum(int a, float b) 
{
    return a + b;
}

float sum(float a, int b) 
{
    return a + b;
}
"""


"""
Method Overloading
"""


class Geometry():
    def calculateArea(self, length):
        print(length * length)

class Square(Geometry):
    pass
    
class Rectangle(Geometry):
    def calculateArea(self, length, breadth):
        print(length * breadth)

square = Square()
rectangle = Rectangle()

square.calculateArea(5)
rectangle.calculateArea(5, 6)
