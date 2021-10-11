#from math import pi 
# save
class Geometry(): #parent class
    def area(self):
        pass
    def perimeter(self):
        pass
    
    
class Circle(Geometry):#child class
    def __init__(self,x,y ,radius):
       self.x=x
       self.y=y
       self.radius=radius

    def area(self):
        "Caculate the area of the circle"
        return 3.1415* self.radius**2  #pi=3.1415 

    def perimeter(self):
        "Caculate the perimeter of the circle"
        return 2*3.1415*self.radius 

    def move(self,deltaX,deltaY):
        self.x +=deltaX
        self.y +=deltaY   
        
    #def __str__(self): 
	   # return 'Circle with coordinates {x}, {y}, and radius {radius} '.format(self.x, self.y, self.radius )    
        
x=4
y=2        
radius = 3
Circle=Circle(x,y,radius)
print (f"Circle with coordinates point at x= {x},y={y},Perimeter of a circle is {Circle.perimeter()},when the radius={radius}")
print (f"Circle with coordinates point at x= {x},y={y},Area of a circle is {Circle.area()},when the radius={radius}")

deltaX=3
deltaY=5
Circle.move(deltaX,deltaY)
print(f"After move,new X:{Circle.x}")
print(f"After move,New Y:{Circle.y}")
# print(Circle.y)


class Rectangle(Geometry):
     def __init__(self,x,y,length,width):
           self.x=x
           self.y=y
           self.length=length
           self.width=width
           
     def area(self):
         "Caculate the area of the rectangle"
         return self.length*self.width

     def perimeter(self):
         "Caculate the perimeter of the rectangle"
         return (self.length+self.width)*2  

     def move(self,deltaX,deltaY):
        self.x +=deltaX
        self.y +=deltaY       

x=5
y=8
length=10
width=6   
  
Rectangle=Rectangle(x,y,length,width)     
#print(Rectangle.x)

print (f"Rectangle with length={length},width={width} at the coordinates x={x},y={y},Perimeter of a Rectangle is {Rectangle.perimeter()}")
print (f"Rectangle with length={length},width={width} at the coordinates  x={x},y={y},Area of a Rectangle is {Rectangle.area()}")
deltaX=3
deltaY=5
Rectangle.move(deltaX,deltaY)
print(f"After move,New X:{Rectangle.x}")
print(f"After move,New Y:{Rectangle.y}")


class Square(Geometry):
     def __init__(self,x,y,side):
           self.x=x
           self.y=y
           self.side=side

           
     def area(self):
         "Caculate the area of the Square"
         return (self.side*self.side)

     def perimeter(self):
         "Caculate the perimeter of the Square"
         return (4*self.side )

     def move(self,deltaX,deltaY):
        self.x +=deltaX
        self.y +=deltaY       

x=-5
y=-8
side=9
 
  
Square=Square(x,y,side)     
#print(Square.x)

print (f"Square with side={side}, at the coordinates x={x},y={y},Perimeter of a Square {Square.perimeter()}")
print (f"Square with side={side}, at the coordinates x={x},y={y},Area of a Square {Square.area()}")
deltaX=3
deltaY=5
Square.move(deltaX,deltaY)
print(f"After move,New X:{Square.x}")
print(f"After move,New Y:{Square.y}")




class Spheres():
    def __init__(self, x,y ,radius):
        self.x=x
        self.y=y
        self.radius = radius
        #self.area = 0
        #self.volume = 0


    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        """Caculate the surface area of the spheres"""
        
        self.area = 4 * 3.14 * (radius*radius)
        return (self.area)

    def Volume(self):
        """Caculate the Volume area of the spheres"""
        self.volume = (4/3) * 3.14 * (radius *radius*radius)
        return (self.volume)
        
x=10
y=2        
radius = 3
Spheres=Spheres(x,y,radius)
print(Spheres.surfaceArea())
print(Spheres.Volume())

print (f"The surface area of Spheres with radius={radius} is {Spheres.surfaceArea()}")
print (f" The volume of Spheres with radius={radius} is {Spheres.Volume()}")
#print (f"Circle with coordinates point at x= {x},y={y},Area of a circle is {Circle.area()},when the radius={radius}")