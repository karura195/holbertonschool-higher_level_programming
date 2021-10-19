#!/usr/bin/python3
"""class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """define square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """square size"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """square arguments"""
        list = ["id", "width", "x", "y"]
        for i in range(len(args)):
            setattr(self, list[i], args[i])
        if len(args) == 0:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """__str__ for square"""
        return ("[Square] {:d} {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    def to_dictionary(self):
        """Square dictionary"""
        key_list = ["id", "size", "x", "y"]
        value_list = [self.id, self.width, self.x, self.y]
        return dict(zip(key_list, value_list))
