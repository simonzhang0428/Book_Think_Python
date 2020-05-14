from turtle import *
import turtle
import math
from math import *

bob = turtle.Turtle()

# first write a small program with NO function definition
for i in range(4):
    bob.fd(100)
    bob.lt(90)


# Encapsulation
# similar pieces in a function
def square(t):
    for side in range(4):
        t.fd(100)
        t.lt(90)


# square(bob)


# Generalization
# function add parameter
def square(t, length):
    for side in range(4):
        t.fd(length)
        t.lt(90)


# square(bob, 100)


def polygon(t, n, length):
    for side in range(n):
        angle = 360 / n
        t.fd(length)
        t.lt(angle)


# keyword argument, include the parameter name as "keyword"
# polygon(bob, n=6, length=100)


def circle(t, r):
    circumference = 2 * pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


# Refactoring
# rearranging a program to improve interfaces and facilitate code reuse
def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon2(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)


# Docstring / Interface
# It is terse, but it contains the essential information
# someone would need to use this function.
# It explains concisely what the function does
# (without getting into the details of how it does it).
# It explains what effect each parameter has on the behavior of the function
# and what type each parameter should be (if it is not obvious).
def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


def circle2(t, r):
    arc(t, r, 360)


# circle(bob, 100)
# arc(bob, 100, 180)

def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()
