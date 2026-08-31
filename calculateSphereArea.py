import math
## program to calculate the volume of a sphere using exponential operators

pi = math.pi
radius = float(input("Enter the radius of the sphere in cm: "))
## typecasts the input to a float

volume = 4/3 ** radius ** 3
## calculates the volume of the sphere using the formula. I chose to use 22/7 as an approximation of pi instead of importing the math module

print("The volume of the sphere is", volume)
## PRINT STATEMENT