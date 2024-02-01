#!/usr/bin/python3
"""module for rectangle class"""


class Rectangle:
    """defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def __init__(self, width=0, height=0):
        """Method to Instantiation width & height"""
        self.width = width
        self.height = height
        self.print_symbol2 = Rectangle.print_symbol
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
            rec += str(self.print_symbol) * self.width + '\n'
        return rec.rstrip('\n')

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
