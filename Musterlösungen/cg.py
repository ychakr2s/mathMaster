import sys
import math


def add_v(x,y):

    return [x[0] + y[0], x[1] + y[1], x[2] + y[2]]


def sub_v(x,y):

    return [x[0] - y[0], x[1] - y[1], x[2] - y[2]]


def sm(a,x):

    return [a*x[0], a*x[1], a*x[2]]


def mv(A,b):
 
    return [A[0][0]*b[0] + A[0][1]*b[1] + A[0][2]*b[2], A[1][0]*b[0] + A[1][1]*b[1] + A[1][2] * b[2], A[2][0]*b[0] + A[2][1]*b[1] + A[2][2] * b[2]]


def sp(x,y):

    prod = 0.0

    for i in range(len(x)):
        prod += x[i] * y[i]
 
    return prod


def norm(x):
 
    return math.sqrt(sp(x,x))


A = [[6,1,2],[1,1,-2],[2,-2,8]]

b = [-2,1,2]

x0 = [1,0,0]

tol = 1e-12

x = list(x0)
Ax = mv(A,x)
r = sub_v(b, Ax)
d = list(r)
k = 0

print "k = ", k
print "x = ", x
print "r = ", r
print "d = ", d
print

while norm(r) > tol:
      k += 1
      Ad = mv(A,d)
      dAd = sp(d,Ad)
      alpha = sp(r,d)/dAd

      x = add_v(x,sm(alpha,d))
   
      Ax = mv(A,x)
      r = sub_v(b,Ax)
      beta = - sp(r,Ad)/dAd      
      d = add_v(r,sm(beta,d))

      print "k = ", k
      print "alpha = ", alpha
      print "x = ", x
      print "r = ", r
      print "beta = ", beta
      print "d = ", d
      print



print "Loesung: x = ", x 
