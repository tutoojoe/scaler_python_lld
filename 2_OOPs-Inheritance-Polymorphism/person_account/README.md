# Person Class Implementation in Python
## Problem Statement
You are tasked with implementing a Python class for managing personal information. The class should allow constructing objects with a variable number of parameters using *args. The constructor should initialize the name attribute for all objects and optionally the age attribute if provided. If the number of arguments is not exactly one or two, an IndexError should be raised.

Your task is to implement a Person class with the following specifications:

### Requirements
### The Person class should have two data members:
* name: String (representing the person's name)
* age: int (representing the person's age, optional)
### The Person class should have one constructor:
* `__init__`: This constructor should accept a variable number of parameters (*args). If there is only one argument, it should initialize the name attribute. If there are two arguments, it should initialize both the name and age attributes. If there are more than two or zero arguments, it should raise an IndexError.
### Instructions
* Implement the Person class according to the specified requirements.
* Ensure that the class contains the specified data members and constructor.
* The constructor should handle variable numbers of arguments using *args.
* Raise an IndexError if the number of arguments is not exactly one or two.