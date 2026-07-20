import math

def rectangle_area(length: float, width: float)->area:
    return length*width

def circle_area(radius:float)->area:
    return radius**2*math.pi

def tri_area(base:float,height:float)->area:
    return .5*base*height