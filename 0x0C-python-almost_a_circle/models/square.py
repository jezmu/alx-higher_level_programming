#!/usr/bin/python3
"""This module contains the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates square's values
        If args exists and is not empty, kwargs is skipped,
        else kwargs is used.
        Order of args:
        - id
        - size
        - x
        - y
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                elif k == 3:
                    self.y = v
                else:
                    break  # don't loop over excess args
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """Returns Square string representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    def to_dictionary(self):
        """Returns Square dictionary representation
        Returned dictionary has the keys:
        - id
        - size
        - x
        - y
        """
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
