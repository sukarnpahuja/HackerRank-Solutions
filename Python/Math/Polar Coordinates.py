# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = input()

#to convert into complex form, use complex()
#polar coordinates = (abs(x),phase(x))

print(abs(complex(z)))
print(cmath.phase(complex(z)))
