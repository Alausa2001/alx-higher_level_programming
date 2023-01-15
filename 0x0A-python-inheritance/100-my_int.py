#!/usr/bin/python3
"""class that overides python's builtin class int"""


class MyInt(int):
    """inherits from int"""

    def __eq__(self, value):
        """overrides the '==' operator"""
        return self.real != value

    def __ne__(self, value):
        """overrides the '!=' operator"""
        return self.real == value
