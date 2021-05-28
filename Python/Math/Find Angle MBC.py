# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)
#M is the midpoint
H = H/2
BC_half = BC/2   #forming 90 degrees

#determining the angle by cosine function
angle = int(round(math.degrees(math.acos(BC_half/H))))

angle = str(angle)

print(angle+ u"\N{DEGREE SIGN}")
