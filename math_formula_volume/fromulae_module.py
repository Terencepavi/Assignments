

import math

def area_of_circle(radius):
    # result=3.14*radius*radius
    result=math.pi*radius**2
    return result
def area_of_square(length):
    result=length*length
    return result
def area_of_triangle(base,height):
    result=(base*height)/2
    return result
def volume_of_cylinder(radius,height):
    result=math.pi*(radius**2)*height
    return result
def volume_of_hemishere(radius):
    result=(2/3)*math.pi*(radius**3)
    return result
def volume_of_sphere(radius):
    result=(4/3)*math.pi*(radius**3)
    return result
def volume_of_cuboid(length,width,height):
    result=length*width*height
    return result
