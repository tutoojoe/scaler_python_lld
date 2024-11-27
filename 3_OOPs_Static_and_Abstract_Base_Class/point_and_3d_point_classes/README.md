# Point and 3D Point Classes
## Problem Statement
You are tasked with creating a Python class hierarchy for representing points in a 2D and 3D coordinate system. The system should provide functionality for initializing and displaying the coordinates of points.

## Requirements

1. Point class:
    - Attributes:`_x, _y`
    - Methods:
        - `__init__(self, x, y)`: Constructor to initialize the point's x and y coordinates.
        - `display(self)`: Prints the point's coordinates in the format [x, y].
2. ThreedPoint class (derived from Point):
    - Attributes: _z (in addition to _x and _y inherited from Point)
    - Methods:
        - `__init__(self, x, y, z)`: Constructor to initialize the 3D point's x, y, and z coordinates. Use `super()` to call the constructor of the base class.
        - `display(self)`: Prints the 3D point's coordinates in the format [x, y, z].
        
## Instructions
- Implement the ThreedPoint class according to the specified requirements. The Point class is already provided.
- Ensure that the ThreedPoint class inherits from the Point class and overrides the necessary methods.
