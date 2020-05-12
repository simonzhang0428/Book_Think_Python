import turtle
import math
from math import *

bob = turtle.Turtle()


# print(bob)
# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)
# turtle.mainloop()


# def square(t):
#     print(t)
#     for side in range(4):
#         t.fd(100)
#         t.lt(90)
#
#
# square(bob)


# def square(t, length):
#     for side in range(4):
#         t.fd(length)
#         t.lt(90)
#
#
# square(bob, 100)


def polygon(t, length, n):
    for side in range(n):
        t.fd(length)
        t.lt(360 / n)


# polygon(bob, 100, 6)
def circle(t, r):
    polygon(t, 2 * pi * r / 100, 100)


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


# circle(bob, 100)
arc(bob, 100, 180)
turtle.mainloop()
