import math

#to calculate area and perimeter of square
class Square:

    
    def CalculateArea(self):
        self.s = int(input("Enter the length of the side: "))
        area = self.s ** 2
        return area
    def CalculatePerimeter(self):
        perimeter  = 4 * self.s
        return perimeter

#to calculate area and perimeter of rectangle    
class Rectangle:

    
    def CalculateArea(self):
        self.width = int(input("Enter width: "))
        self.height = int(input("Enter Height: "))
        area = self.height * self.width
        return area
    def CalculatePerimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter


#to calculate area and perimeter of circle    
class Circle:

    
    def CalculateArea(self):
        self.radius = int(input("Enter radius: "))
        area = math.pi * (self.radius**2)
        return area
    def CalculatePerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

 #to calculate area and perimeter of ellipse   
class Ellipse:

    
    def CalculateArea(self):
        self.smax = int(input("Enter axis x: "))
        self.smay = int(input("Enter axis y: "))
        area = math.pi * self.smax * self.smay
        return area
    def CalculatePerimeter(self):
        perimeter = 2*math.pi * math.sqrt(((self.smax)**2 + (self.smay)**2)/2)
        return perimeter
    

s = Square()
r = Rectangle()
c = Circle()
e = Ellipse()
a_s = s.CalculateArea()
p_s = s.CalculatePerimeter()
a_r = r.CalculateArea()
p_r = r.CalculatePerimeter()
a_c = c.CalculateArea()
p_c = c.CalculatePerimeter()
a_e = e.CalculateArea()
p_e = c.CalculatePerimeter()

#to calculate area and perimeter of square,rectangle,circle,ellipse
print(f"The area of square is {a_s}")
print(f"The perimeter of square is {p_s}")
print(f"The area of rectangle is {a_r}")
print(f"The perimeter of rectangle is {p_r}")
print(f"The area of circle is {a_c}")
print(f"The perimeter of circle is {p_c}")
print(f"The area of ellipse is {a_e}")
print(f"The perimeter of ellipse is {p_e}")


    
