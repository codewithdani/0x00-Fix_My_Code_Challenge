#!/usr/bin/python3
""" Module for square class """


class Square():
    """ Square class """
    width = 0
    hieght = 0

    def __init__(self, *args, **kwargs):
        """ Instantiation of class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ Permiter of the square """
        return 4 * self.width

    def __str__(self):
        """ Printable representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square object """
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.permiter_of_my_square())
