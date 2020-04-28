import math
print("To get the distance between two points, enter a X,Y value")

x1 = float(input( "X coordinates "))
y1 = float(input( "Y cordinates "))

print("Now enter the X,Y value for the second point")

x2 = float(input( "X coordinates "))
y2 = float(input( "Y coordinates "))

print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
