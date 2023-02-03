import Shapes3D
import Shapes
import csv

#Solver
class Solver:
    total = 0
    shapeList = []

    with open("input.csv", mode ='r')as file:
        csvFile = csv.reader(file, delimiter=',')
        for lines in csvFile:
            #print(lines)
            if lines[0] == "cube":
                shapeList.append(Shapes3D.Cube(float(lines[1])))                
            elif lines[0] == "cuboid":
                shapeList.append(Shapes3D.Cuboid(float(lines[1]), float(lines[2]), float(lines[3])))
            elif lines[0] == "prism":
                shapeList.append(Shapes3D.Prism(float(lines[1]), float(lines[2]), float(lines[3])))
            elif lines[0] == "cylinder":
                shapeList.append(Shapes3D.Cylinder(float(lines[1]), float(lines[2])))
            elif lines[0] == "sphere":
                shapeList.append(Shapes3D.Sphere(float(lines[1])))            
            elif lines[0] == "area":
                for shape in shapeList:
                    total += shape.GetArea() * float(lines[1])
            elif lines[0] == "volume":
                for shape in shapeList:
                    total += shape.GetVolume() * float(lines[1])

    print(total)