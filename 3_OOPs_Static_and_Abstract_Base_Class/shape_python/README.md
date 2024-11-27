# Shape Class Implementation in Python

## Problem Statement
Implement an abstract class `Shape` in Python along with child classes like `Rectangle` and `Circle`. `Shape` is an abstract class with abstract methods `area()` and `perimeter()`. `Rectangle` and `Circle` are child classes of `Shape`, implementing the `area()` and `perimeter()` methods specific to their shapes. 
- `Rectangle` takes length and width as parameters.
- `Circle` takes radius as a parameter.

## Requirements
- Implement an abstract class `Shape` with the following abstract methods:
  - `area()`: Calculates the area of the shape.
  - `perimeter()`: Calculates the perimeter of the shape.
- Implement child classes `Rectangle` and `Circle` inheriting from `Shape`.
- `Rectangle` should have a constructor that accepts length and width.
- `Circle` should have a constructor that accepts the radius.

## Instructions
- Implement the `Shape`, `Rectangle`, and `Circle` classes according to the specified requirements.
- Ensure that the `Shape` class contains the abstract methods `area()` and `perimeter()`.
- Ensure that the `Rectangle` class properly implements the `area()` and `perimeter()` methods for rectangles.
- Ensure that the `Circle` class properly implements the `area()` and `perimeter()` methods for circles.
- Use `math.pi` as the value of pi for calculating the area of a circle.
