#!/usr/bin/python3
"""contains a class that inherits ``list``"""


class MyList(list):
    """class whose superclass is ``list``"""

    def __init__(self):
        """initilizes the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""

        c = []
        for i in self:
            c. append(i)
        print(sorted(c))
