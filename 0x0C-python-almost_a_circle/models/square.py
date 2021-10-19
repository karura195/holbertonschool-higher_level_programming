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
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """square arguments"""
        args_list = ["id", "width", "x", "y"]
        for i in range(len(args)):
            setattr(self, list[i], args[i])
        if len(args) == 0:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """__str__ for square"""
        return ("[Square] {:d} {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))
