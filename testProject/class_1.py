import math


class Circle:
    """ Represents a circle.

    attributes: center, radius
    """


class Point:
    """ Represents a circle.

    attributes: x, y
    """


def distance_between_points(point1, point2):
    return math.sqrt(abs((point1.x - point2.x)**2 + (point1.y - point2.y)**2))


def point_in_circle(circle, point):
    """ Принимает в качестве аргументов объекты Circle и Point и возвращает True,
    если Point лежит внутри круга или на его границе
    """
    distance = distance_between_points(circle.center, point)
    if distance <= circle.radius:
        return True
    else:
        return False


# circle definition
circle = Circle()
circle.center = Point()
circle.radius = 75
circle.center.x = 150
circle.center.y = 100

# circle definition
point = Point()
point.x = 160
point.y = 120

print(point_in_circle(circle, point))
