from turtle import *
from math import *

#init turtle
T=Turtle()


#sample size
T.screen.setworldcoordinates(-1,-1,1,1) 

#speed up the turtle
T.speed(-1)

#range of hundredths from -1 to 1
xcoords=map(lambda x: x/100.0,xrange(-100,101))
print xcoords

#setup the origin
T.pu();T.goto(-1,0);T.pd()

#move turtle
for x in xcoords:
    T.goto(x,sin(xcoords.index(x)))
