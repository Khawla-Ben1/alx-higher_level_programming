#!/usr/bin/python3
"""
Define a Rectangle
"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print the rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        size = str(self.print_symbol) * self.width
        return "\n".join([size] * self.height)

    def __repr__(self):
        """Return representation of the Rectangle"""
        return "{:s}({:d}, {:d})".format(
            type(self).__name__,
            self.width,
            self.height
            )

    def __del__(self):
        """Delete the Rectangle, decrease instance count"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle,
        or return None if height/width are 0"""
        if self.height == 0 or self.width == 0:
            return None
        return (self.height * 2) + (self.width * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the larger rectangle after comparing"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Initialize a new square instance"""
        return cls(size, size)
