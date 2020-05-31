import copy
from math import sqrt


class Point:
    """Represent a point in 2-D space."""


print(Point)  # <class '__main__.Point'>

blank = Point()  # instantiation, instance of class
print(blank)  # <__main__.Point object at 0x103f869a0>

blank.x = 3.0
blank.y = 4.0


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


print_point(blank)


def distance_between_points(p1, p2):
    return round(sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2), 2)


p1 = Point()
p1.x = 6
p1.y = 9
print(distance_between_points(blank, p1))


class Rectangle:
    """Represent a rectangle.

    attributes: width, height, corner.
    """


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


center = find_center(box)
print_point(center)

box.width = box.width + 50
box.height = box.height + 100


def grow_rectangle(rect, dwitdth, dheight):
    rect.width += dwitdth
    rect.height += dheight


print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)


def move_rectangle(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x = rect.corner.x + dx
    new_rect.corner.y = rect.corner.y + dy
    return new_rect


move_rectangle(box, 50, 100)
print(box.corner.x, box.corner.y)

p2 = copy.copy(p1)
print_point(p1)
print_point(p2)
print(p1 is p2)  # if the same object
print(p1 == p2)  # False. check identity, not equivalence

box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)  # shallow copy, not embedded object

box3 = copy.deepcopy(box)  # deep copy, every reference is new object
print(box3 is box)
print(box3.corner is box.corner)

box4 = move_rectangle(box, 50, 100)
print(box4.corner is box.corner)
print(box4.corner.x, box4.corner.y)
print(box4.width, box4.height)

print(isinstance(p1, Point))  # check instance of class
print('True:', hasattr(p1, 'x'))  # check attribute, second one must be string
print('False:', hasattr(p1, 'z'))
print('False:', hasattr(box, 'Point'))

# class Circle:
#     """Represent a Circle.
#
#     attributes: center, radius.
#     """
#     center = Point()
#     radius = 0.0
#
#
# c = Circle()
# c.center.x = 150
# c.center.y = 100
# c.radius = 75
#
#
# def point_in_circle(c, p):
#     d = distance_between_points(c.center, p)
#     return d <= c.radius
#
#
# p3 = Point()
# p3.x = 150
# p3.y = 25
# print('False:', point_in_circle(c, p1))
# print('True:', point_in_circle(c, p3))
#
#
# def rect_in_circle(c, rect):
#     return point_in_circle(c, rect.corner) and \
#            point_in_circle(c, move_rectangle(rect, rect.weight, 0).corner) and \
#            point_in_circle(c, move_rectangle(rect, 0, rect.height).corner)
#
#
print('#' * 20)


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
