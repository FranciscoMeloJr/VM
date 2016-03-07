import math
import turtle

ws = turtle.Screen()
ws.bgcolor("lightblue")
fred = turtle.Turtle()
for angle in range(360):
    y = math.sin(math.radians(angle))
    fred.goto(angle, y * 190)

ws.exitonclick()
