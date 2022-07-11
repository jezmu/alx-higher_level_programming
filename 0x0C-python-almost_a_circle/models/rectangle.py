#!/usr/bin/python3
"""Contains Rectangle class definition"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a rectangle
        Args:
            width: rectangle width
            height: rectangle height
            x: x offset
            y: y offset
            id: rectangle instance's id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.validate_int("width", value)
        self.validate_gt_zero("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validate_int("height", value)
        self.validate_gt_zero("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validate_int("x", value)
        self.validate_gte_zero("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.validate_int("y", value)
        self.validate_gte_zero("y", value)
        self.__y = value

    def validate_int(self, name, value):
        """checks whether a value is an integer
        Throws:
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def validate_gt_zero(self, name, value):
        """checks whether a value is greater than zero
        Throws:
            ValueError: if value is <= 0
        """
        if value <= 0:
            raise ValueError("{:s} must be > 0".format(name))

    def validate_gte_zero(self, name, value):
        """checks whether a value is greater than or equal to zero
        Throws:
            ValueError: if value is < 0
        """
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """returns rectangle's area"""
        return self.width * self.height

    def convert_to_str(self):
        """Converts rectangle to printable character representation"""
        rect = "\n" * self.y + "\n".join(
            (" " * self.x + "#" * self.width) for row in range(self.height)
        )
        return rect

    def display(self):
        """prints out rectangle instance"""
        print(self.convert_to_str())

    def __str__(self):
        """Returns Rectangle string representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """updates rectangles' values
        The order of args is:
        - id
        - width
        - height
        - x
        - y
        If args exists and is not empty, the kwargs are skipped
        """
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i > 4:  # no need to loop over excess args
                    break
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns Rectangle dictionary representation"""
        d = {}
        d["id"] = self.id
        d["x"] = self.x
        d["y"] = self.y
        d["width"] = self.width
        d["height"] = self.height
        return d
