class Geometry(): #parent class
    def area(self):
        pass
    def perimeter(self):
        pass
    def volum(self):
        pass

    def is_number():
         try:
             float
             return True
         except ValueError:
             return False   
             
    def is_possiblenumber
    
    
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

      #check if a point lies inside the circle
    def is_inside(self,givenX,givenY,x,y,radius): # at given point
        self.givenX=givenX
        self.givenY=givenY
        self.x=x
        self.y=y
        self.radius=radius
        
        if((givenX-x)*2+ (givenY-y)*2<=radius*2):
            return True;
        else:
             return False;   

    def __repr__  (self):      
        return (f"Circle(x='{self.x}',y='{self.y}', radius='{self.radius}')")

    

        
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

givenX=8
givenY=6

is_inside=Circle.is_inside(givenX,givenY,x,y,radius)
print(f"New point at ({givenX},{givenY}),is {is_inside} of the inside of the circle with coordinates at x= {x},y={y},radius={radius}")



# 正方型的点
class Rectangle():
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

     
     def is_inside(self,givenX,givenY,x,y): # at given point
        self.givenX=givenX
        self.givenY=givenY
        self.x=x
        self.y=y
        
        
        if(x/2-givenX<=x <=x/2+givenX) and (y/2-givenY<=y <=y/2+givenY):
        
            return True;
        else:
             return False;    
#middle point(x,y)
x=5
y=8
length=10
width=6   

givenX=28
givenY=8
  
Rectangle=Rectangle(x,y,length,width)     
#print(Rectangle.x)

print (f"Rectangle with length={length},width={width} at the coordinates x={x},y={y},Perimeter of a Rectangle is {Rectangle.perimeter()}")
print (f"Rectangle with length={length},width={width} at the coordinates  x={x},y={y},Area of a Rectangle is {Rectangle.area()}")
deltaX=3
deltaY=5
Rectangle.move(deltaX,deltaY)
print(f"After move,New X:{Rectangle.x}")
print(f"After move,New Y:{Rectangle.y}")

is_inside=Rectangle.is_inside(x,y,givenX,givenY)
print(f"New point at ({givenX},{givenY}),is {is_inside} of the inside of the rectangle with middle point at x= {x},y={y}")