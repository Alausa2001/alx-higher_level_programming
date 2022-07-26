#!/usr/bin/python3
"""
Locked class
"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attribute
    except if the instance attribute is first_class
    """
    __slots__ = ["first_name"]
