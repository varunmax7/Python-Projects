#Program file 1
import Mechanical_Cal_Circle
r = int(input("Enter the radius of circle: "))
print("Circle area and perimeter is: ")
print(Mechanical_Cal_Circle.circle_area(r))
print(Mechanical_Cal_Circle.circle_perimeter(r))
#Program file 2
import Mechanical_Cal_Circle as mcc
r = int(input("Enter the radius of the circle: "))
print(mcc.circle_area(r))
print(mcc.circle_perimeter(r))
#Program file 3
from Mechanical_Cal_Circle import circle_area
r = int(input("Enter the radius of the circle; "))
print("Area of the circle: ")
print(circle_area(r))
#Program file 4
from Mechanical_Cal_Circle import *
r = int(input("Enter the radius of the circle: "))
print("circle area and perimeter is: ")
print(circle_area(r))
print(circle_perimeter(r))

