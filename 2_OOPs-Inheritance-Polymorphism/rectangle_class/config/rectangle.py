import copy


from .point import Point


class Rectangle:
    def __init__(self, *args):
        """
        Initialize a Rectangle object.

        Args:
            *args: Variable number of arguments. The constructor can be called in three ways:
                - With two Point objects representing the top-left and bottom-right corners.
                - With four integers representing the x and y coordinates of the top-left and bottom-right corners.
                - With a single Rectangle object for copying.

        Raises:
            ValueError: If invalid arguments are provided.
        """
        if len(args) == 2 and all(isinstance(arg, Point) for arg in args):
            # Initializing with two Point objects
            self.topLeft = copy.deepcopy(args[0])
            self.bottomRight = copy.deepcopy(args[1])
        elif len(args) == 4 and all(isinstance(arg, int) for arg in args):
            # Four integer coordinates (x1, y1, x2, y2)
            self.topLeft = Point(args[0], args[1])
            self.bottomRight = Point(args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], Rectangle):
            # A single Rectangle object
            self.topLeft = copy.deepcopy(args[0].topLeft)
            self.bottomRight = copy.deepcopy(args[0].bottomRight)

        else:
            # Invalid arguments
            raise ValueError("Invalid arguments for Rectangle initialization")

            # Validation to ensure topLeft is actually above and to the left of bottomRight
        if not (self.topLeft.x < self.bottomRight.x and self.topLeft.y < self.bottomRight.y):
            raise ValueError("Invalid rectangle corners: top-left should be above and to the left of bottom-right")

    # Initializing with four integer coordinates

