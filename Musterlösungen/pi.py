from math import sqrt
import sys

r = 0.5
a = r*sqrt(2) # n = 2

for n in range(3,20):

    h = sqrt(pow(r,2) - pow(a,2)/4.0)
     
    a = sqrt(pow(a,2)/4.0 + pow(r-h,2))
    
    print a*pow(2,n)
