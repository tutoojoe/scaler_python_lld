import copy


class Point:
    def __init__(self, x, y):
        # TODO: Initialize the Point class with x and y coordinates
        self.x = x
        self.y = y

    def __eq__(self, other):
        # TODO: Implement equality comparison between two points
        return True if self.x == other.x and self.y == other.y else False

    def __str__(self):
        # TODO: Return a string representation of the point in the format "(x, y)"
        return f"({self.x}, {self.y})"

    def __copy__(self):
        # TODO: Create a shallow copy of the point

        return Point(self.x, self.y)

    def __deepcopy__(self, memo):
        # TODO: Create a deep copy of the point using the copy module
        # deep_copy = copy.deep_copy(memo)
        # return deep_copy

        if id(self) in memo:
            return memo[id(self)]

        # Create a deep copy of the Point instance
        copy_obj = Point(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))
        # Store the copy in the memo dictionary to avoid circular reference issues
        memo[id(self)] = copy_obj
        return copy_obj
