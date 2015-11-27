"""
Write a function named move_rectangle that takes a
Rectangle and two numbers
named dx and dy. It should change the location of
the rectangle by adding dx to the x coordinate of
corner and adding dy to the y coordinate of corner.
"""


class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """


class Point(object):
    """Represents a point in 2-D space."""
    # basically an object which we can manipulate


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print_point(blank)

    rec = Rectangle()
    rec.width = 100.0
    rec.height = 200.0
    print(rec.width)
    print(rec.height)
    print('grow')
    grow_rectangle(rec, 50, 100)
    print(rec.width)
    print(rec.height)

main()
