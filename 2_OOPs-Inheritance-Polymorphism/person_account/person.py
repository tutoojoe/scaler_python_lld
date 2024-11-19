class Person:
    # TODO: Implement the constructor to initialize the name attribute for all objects
    #       and optionally the age attribute if provided.
    #       Raise an IndexError if the number of arguments is more than 2 or zero.
    def __init__(self, *args):
        if len(args) < 1 or len(args) > 2:
            raise IndexError
        self.name = args[0]

        if len(args) > 1:
            self.age = args[1]
