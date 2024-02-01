#!/usr/bin/python3
"""module for rectangle class"""


class Rectangle:
    """defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method to Instantiation width & height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

        @property
        def width(self):
            """property retrieve width"""
            return self.__width

        @width.setter
        def width(self, value):
            """set width value"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """property retreive height"""
            return self.__height

        @height.setter
        def height(self, value):
            """set height value"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """return rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        rec = ""
        for i in range(self.height):
            rec += str(Rectangle.print_symbol) * self.width + '\n'
        return rec.rstrip('\n')

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
