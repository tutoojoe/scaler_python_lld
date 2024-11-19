class Math:
    PI = 3.14

    # TODO: Implement the given method to calculate the area of circle
    @staticmethod
    def getCircleArea(radius):
        # note: in order to use the class variable, we have to mention the class_name.variable name format
        area = Math.PI * radius * radius
        return area
