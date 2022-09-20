class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.r = radius
           
    def circumference(self):
        return 2*Circle.pi*self.r

    def area(self):
        return Circle.pi*self.r*self.r

c = Circle(56)
print(c.area())


