"""
Write a version of move_rectangle that creates
and returns a new Rectangle
instead of modifying the old one.
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

    #or Create a new Reactangle object

    rec2= Rectangle()
    rec2.width=rec.width+55
    rec2.height=rec.height+111
    print("Using another object: Results")
    print(rec2.width)
    print(rec2.height)

main()
