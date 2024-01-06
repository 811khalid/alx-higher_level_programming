Python - More Classes and Objects
This repository focuses on learning and practicing object-oriented programming in Python. It covers various topics such as class methods, static methods, class vs instance attributes, and the usage of special methods like __str__ and __repr__.

Tests :heavy_check_mark:
tests: This folder contains test files provided by Holberton School.
Tasks :page_with_curl:
0. Simple rectangle

0-rectangle.py: An empty Python class that serves as the basic definition of a rectangle.
1. Real definition of a rectangle

1-rectangle.py: A Python class that defines a rectangle. It builds upon 0-rectangle.py and includes the following features:
A private instance attribute called width.
A property getter method def width(self): that retrieves the value of width.
A property setter method def width(self, value): that sets the value of width.
A private instance attribute called height.
A property getter method def height(self): that retrieves the value of height.
A property setter method def height(self, value): that sets the value of height.
An instantiation method def __init(self, width=0, height=0): that initializes the rectangle with optional width and height parameters.
If either width or height is not an integer, a TypeError is raised with the message width must be an integer or height must be an integer.
If either width or height is less than 0, a ValueError is raised with the message width must be >= 0 or height must be >= 0.
2. Area and Perimeter

2-rectangle.py: A Python class that defines a rectangle. It builds upon 1-rectangle.py and includes the following features:
A public instance method def area(self): that calculates and returns the area of the rectangle.
A public instance method def perimeter(self): that calculates and returns the perimeter of the rectangle. If either width or height equals 0, the perimeter is 0.
3. String representation

3-rectangle.py: A Python class that defines a rectangle. It builds upon 2-rectangle.py and includes the following features:
A special method __str__ that allows the rectangle to be printed using the # character. If either width or height equals 0, the method returns an empty string.
4. Eval is magic

4-rectangle.py: A Python class that defines a rectangle. It builds upon 3-rectangle.py and includes the following features:
A special method __repr__ that returns a string representation of the rectangle.
5. Detect instance deletion

5-rectangle.py: A Python class that defines a rectangle. It builds upon 4-rectangle.py and includes the following features:
A special method __del__ that prints the message Bye rectangle... when a Rectangle instance is deleted.
6. How many instances

6-rectangle.py: A Python class that defines a rectangle. It builds upon 5-rectangle.py and includes the following features:
A public class attribute number_of_instances that is initialized to 0 and is incremented for each new instantiation of a rectangle. It is decremented for each instance deletion.
7. Change representation

7-rectangle.py: A Python class that defines a rectangle. It builds upon 6-rectangle.py and includes the following features:
A public class attribute class_symbol that is initialized to #. This attribute can be of any type and is used as the symbol for string representation of the rectangle.
8. Compare rectangles

8-rectangle.py: A Python class that defines a rectangle. It builds upon 7-rectangle.py and includes the following features:
A static method def bigger_or_equal(rect_1, rect_2): that compares two rectangles and returns the rectangle with the greater area. If both rectangles have equal areas, it returns rect_1.
If either rect_1 or rect_2 is not an instance of the Rectangle class, a TypeError is raised with the message rect_1 must be an instance of Rectangle or rect_2 must be an instance of Rectangle.
9. A square is a rectangle

9-rectangle.py: A Python class that defines a rectangle. It builds upon 8-rectangle.py and includes the following features:
A class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size.
10. N Queens

alt text
* 101-nqueens.py: A Python program that solves the N queens puzzle. * Usage: ./101-nqueens.py N * This program determines all possible solutions for placing N non-attacking queens on an NxN chessboard. * It requires exactly two arguments to be provided. Otherwise, the program prints Usage: nqueens N and exits with a status of 1. * If the provided N is not an integer, the program prints N must be a number and exits with a status of 1. * If the provided N is less than 4, the program prints N must be at least 4 and exits with a status of 1. * The solutions are printed one per line in the format [[r, c], [r, c], [r, c], [r, c]], where r and c represent the row and column, respectively, where a queen must be placed.
