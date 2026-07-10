import math

def value(diameter, cost):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    value = area/cost if cost != 0 else 00
    return area, value


diameter1=12#float(input("Enter the diameter of the small pizza in inches: "))
cost1    = 8.55#float(input("Enter the cost of the small pizza: "))
diameter2= 18#float(input("Enter the diameter of the large pizza in inches: "))
cost2    = 13.99#float(input("Enter the cost of the large pizza: "))

area1, value1 = value(diameter1, cost1)
area1*=2
area2, value2 = value(diameter2, cost2)

print(f"The area of two small pizzas is {area1:.2f} square inches")
print(f"The area of the large pizza is {area2:.2f} square inches")
print(rf"The value of two small pizzas is {value1:.2f} $\frac{{in^2}}{{\$}}$")
print(rf'The value of the large pizza is {value2:.2f} $\frac{{in^2}}{{\$}}$')