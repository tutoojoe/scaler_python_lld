# Rectangle Class Implementation in Python
## Problem Statement
You are tasked with implementing a Python class for representing rectangles. The class should allow initializing rectangles either by providing coordinates or by passing existing rectangle objects for copying. Additionally, the implementation should robustly handle invalid initialization parameters by raising a ValueError.

Your task is to implement a Rectangle class with the following specifications:

## Requirements
The Rectangle class should have the following data members:
* topLeft: A Point object representing the top-left corner of the rectangle.
* bottomRight: A Point object representing the bottom-right corner of the rectangle.
### The Rectangle class should have one constructor:
* `__init__` : This constructor should accept a variable number of arguments (*args). It should initialize the rectangle either by providing two Point objects representing the top-left and bottom-right corners, four integer coordinates representing the top-left and bottom-right corners, or a single Rectangle object for copying. The constructor must validate the input arguments and raise a ValueError if they do not match any of the expected argument patterns.
## Instructions
* Implement the Rectangle class according to the specified requirements.
* Ensure that the class contains the specified data members and constructor.
* Implement the constructor to initialize the rectangle based on the provided arguments.
* Ensure that the constructor handles different argument combinations correctly and raises a ValueError for invalid inputs.
* Make sure you use the deepcopy method when copying objects within the class to ensure that copies are independent of the original objects.