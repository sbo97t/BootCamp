import math
print("To get the distance between two points, enter an X,Y value")

distx1 = float(input( "X coordinates "))
disty1 = float(input( "Y cordinates "))

print("Now enter the X,Y value for the second point")

distx2 = float(input( "X coordinates "))
disty2 = float(input( "Y coordinates "))

print(math.sqrt((distx2 - distx1)**2 + (disty2 - disty1)**2))
