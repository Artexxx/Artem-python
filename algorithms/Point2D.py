import math


class Point2d(object):
    def __init__(self, dx=0, dy=0):
        """
        Initializer with default values of 0
        """
        self.x = dx
        self.y = dy

    def magnitude(self):
        """
        Return the magnitude of the point, which is the distance from the origin
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def dist(self, o):
        """
        Return the distance between two Point2d objects as a float
        """
        return math.sqrt((self.x - o.x) ** 2 + (self.y - o.y) ** 2)

    def scale(self, s):
        """
        Scale each coordinate of a Point2d object by the numerical scale value.
         This changes the object rather than creating a new object
        """
        self.x *= s
        self.y *= s

    def dominates(self, o):
        """
        Given two Point2d objects return True iff the coordinates of the
        first object are each larger than those of the second
        """
        return self.x > o.x and self.y > o.y

    def __add__(self, o):
        """
        Add the two Point2d object coordinate-wise, returning a new Point2d object.
        """
        return Point2d(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        """
        Subtract the two Point2d object coordinate-wise, returning a new Point2d object.
        """
        return Point2d(self.x - o.x, self.y - o.y)

    def __mul__(self, s):
        """
        Multiply the coordinates of a Point2d object by a scale factor, returning a new Point2d object.
        """
        return Point2d(s * self.x, s * self.y)

    def __eq__(self, o):
        """
        (==) Return True if the coordinate values of the two Point2d objects are the same.
        """
        return self.x == o.x and self.y == o.y

    def slight_lt(self, other):
        """
         Return True if the coordinate values  of at least 1 of the 2 coordinates of the two Point2d objects are the same.
        """
        return self.x_lt(other) or self.y_lt(other)

    def __ne__(self, o):
        """
        (!=) Return True if the coordinate values of the two Point2d objects are the disagree.
        """
        return self.x != o.x or self.y != o.y

    def __gt__(self, o):
        """
        (>) Return True if the coordinate values first object are greater than the second
        """
        return self.x > o.x and self.y > o.y

    def __lt__(self, o):
        """
        (<) Return True if the coordinate values first object are less than the second
        """
        return self.x < o.x and self.y < o.y

    def __ge__(self, o):
        """
        (>=) Return True if the coordinate values first object are greater than or equal than the second
        """
        return self.x >= o.x and self.y >= o.y

    def __le__(self, o):
        """
        (<=) Return True if the coordinate values first object are less than or equal than the second
        """
        return self.x <= o.x and self.y <= o.y

    def __str__(self):
        """
        Create a string representation of a Point2d object.
        """
        return "({},{})".format(self.x, self.y)

    def copy(self):
        """ Copy the Point2d object coordinate-wise, returning a new Point2d object."""
        return Point2d(self.x, self.y)

    def left(self):
        self.x += -1
        return self

    def right(self):
        self.x += 1
        return self

    def up(self):
        self.y += 1
        return self

    def down(self):
        self.y += -1
        return self


if __name__ == "__main__":
    p = Point2d(0, 4)
    q = Point2d(5, 10)
    leng = q.magnitude()
    leng = Point2d.magnitude(q)
    print("Magnitude {:.2f}".format(leng))
    print("Distance is {:.2f}".format(p.dist(q)))

    # Exercise 1 tests:
    p.scale(3)
    print('After scaling p = ({},{})'.format(p.x, p.y))
    r = Point2d(3, 5.5)
    r.scale(2)
    print('After scaling r = ({},{})'.format(r.x, r.y))
    print('p dominates r:', p.dominates(r))
    print('r dominates p:', r.dominates(p))
    print('r dominates q:', r.dominates(q))

    # Exercise 2:  __str__ tests
    print("As a string p is " + str(p))
    print("As a string r is " + str(r))

    # Exercise 2:  other tests
    print('p - q =', str(p - q))
    print('q - r =', str(q - r))
    new_q = q * 4
    print('new_q is', new_q)
    t = Point2d(0, 12)
    u = Point2d(0, 5)
    v = Point2d(5, 12)
    print('p == t', p == t)
    print('t == u', t == u)
    print('t == v', t == v)
