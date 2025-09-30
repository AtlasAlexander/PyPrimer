import math
a= -1
b = 8
c = -1
x1 = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
x2 = (-b - math.sqrt((b**2)-4*a*c))/(2*a)
print("The solutions are both" , str(round(x1,3)), "&" , str(round(x2,3)))

#output - The solutions are both 0.127 & 7.873
