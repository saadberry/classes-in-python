# Trying out Classes in Python
class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        #applying formula
        print(self.x,self.y)
        distance = (((self.x**2)+(self.y**2))**0.5)

        return distance

    def reflect(self,axis):
        if axis == 'x':
            self.y = -(self.y)
        
        elif axis == 'y':
            self.x = -(self.x)

        else:
            print("ERROR!")

# p = Point(2,2)
# x=p.distance_to_origin()
# print(x)

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())