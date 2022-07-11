#!/usr/bin/python3
"""Contains Base class definition"""

import json
import csv


class Base:
    """The base class
    Attributes:
        __nb_objects: number of instantiated base objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates a base class insatnce
        Args:
            id: the id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json representation of a list of dictionaries
        Args:
            list_dictionaries: the list of dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves object instances to a file
        The objects are first converted to json then saved to a file
        Args:
            list_objs: list of objects to save
        """
        data = []
        if list_objs is not None:
            data = [obj.to_dictionary() for obj in list_objs]
        objs_json = cls.to_json_string(data)
        file = cls.__name__ + ".json"
        with open(file, mode="w", encoding="utf-8") as f:
            f.write(objs_json)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation
        Args:
            json_string: the string to be converted to a list
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Instantiates an object with properties from the provided dictionary
        Returns:
            the instantiated object
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads instances from a file
        Returns:
            list of loaded instances if file exists. An empty list is
            returned if required file does not exist
        """
        file = cls.__name__ + ".json"
        objs = []
        try:
            with open(file, "r") as f:
                data = cls.from_json_string(f.read())
                for obj_d in data:
                    objs.append(cls.create(**obj_d))
                return objs
        except OSError:
            pass
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instances to a csv file"""
        file = cls.__name__ + ".csv"
        with open(file, "w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                else:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads object instances from csv file"""
        file = cls.__name__ + ".csv"
        objects = []
        with open(file, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    data = {
                        "id": int(row[0]),
                        "width": int(row[1]),
                        "height": int(row[2]),
                        "x": int(row[3]),
                        "y": int(row[4]),
                    }
                elif cls.__name__ == "Square":
                    data = {
                        "id": int(row[0]),
                        "size": int(row[1]),
                        "x": int(row[2]),
                        "y": int(row[3]),
                    }
                objects.append(cls.create(**data))
        return objects
