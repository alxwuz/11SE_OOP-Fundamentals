from abc import ABC, abstractmethod
 
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass
	
class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
		
	def perimeter(self):
		return 2 * 3.14 * self.radius
	
	def area(self):
		return 3.14 * self.radius ** 2

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
        def perimeter(self):
	        return 2 * (self.width + self.height)
	
	def area(self):
		return self.width * self.height
	
# Creating instances of concrete subclasses 
circle = Circle(5) 
rectangle = Rectangle(4, 6) 

# Using the same interface to compute perimeter 
print("Circle Perimeter:", circle.perimeter()) 
print("Rectangle Perimeter:", rectangle.perimeter()) 