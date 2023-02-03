import math
import csv
import Shapes


#Sphere
class Sphere:
    def __init__ (self, radius:float):
        self.radius = radius
    
    def GetArea(self) -> float:
        return 4 * math.pi *(self.radius * self.radius)
    
    def GetVolume(self) -> float:
        return 2 * math.pi * self.radius

#Cube
class Cube:
    def __init__ (self, sideLengh:float):
        self.sideLengh = sideLengh
    
    def GetArea(self) -> float:
        return 2 * (self.sideLengh * self.sideLengh)
    
    def GetVolume(self) -> float:
        return self.sideLengh * self.sideLengh * self.sideLengh

#Cuboid
class Cuboid:
    def __init__ (self, width:float, height:float, depth:float):
        self.width = width
        self.height = height
        self.depth = depth
    
    def GetArea(self) -> float:
        return 2 *((self.height * self.width) + (self.depth * self.height) + (self.width * self.depth))
    
    def GetVolume(self) -> float:
        return self.width * self.height * self.depth
    
#Prism
class Prism:
    def __init__(self, sides, sideLength, height):
        self.height = height
        self.face = Shapes.Polygon(sides, sideLength).GetArea()
        self.perimeter = Shapes.Polygon(sides, sideLength).GetPerimeter()

    def GetArea(self) -> float:
        return (self.perimeter * self.height) + (2 * self.face)

    def GetVolume(self) -> float:
        return self.face * self.height

#Cylinder
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.base = Shapes.Circle(radius).GetArea()

    def GetArea(self) -> float:
        return (self.base * self.height) + (2 * self.base)

    def GetVolume(self) -> float:
        return self.base * self.height