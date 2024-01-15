Python - Almost a Circle

In this project, I used Python to create three classes that represent rectangles and squares. I wrote my own test suite to check the functionality of each class.

The classes involved various Python tools such as importing modules, handling exceptions, using private attributes, and implementing getter and setter methods. I also utilized class and static methods, inheritance, file input/output, and serialization/deserialization using JSON and CSV formats. Additionally, I performed unit testing using the unittest module.

Classes:

Base:

    The base class for all other classes in the project.
    It includes private and public attributes and provides methods for JSON serialization, file operations, and object instantiation.

Rectangle:

    Represents a rectangle and inherits from the base class.
    It has private attributes for width, height, x-coordinate, and y-coordinate.
    Provides methods for calculating the area, displaying the rectangle, updating its attributes, and converting it to a dictionary.

Square:

    Represents a square and inherits from the rectangle class.
    It has a constructor that takes the size of the square and assigns it to the width and height attributes of the rectangle.
    Provides methods for updating attributes and converting it to a dictionary.

These classes can be used to create and manipulate rectangles and squares in a Python program.
